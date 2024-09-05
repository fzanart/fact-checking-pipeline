"""
Module for detecting fallacies in text.
"""

import os
import re
import time
import json
import csv
from ast import literal_eval
from collections import namedtuple
import requests
from .templates import (
    FACTUAL_RESPONSE,
    INCONTEXT,
    SUMMARIZATION,
    CONCLUDING,
    CONCLUDING_INCONTEXT,
)
from .definitions import DEFINITIONS
from .examples import FALLACY_CLAIMS, DEBUNKINGS
from ..fact_check.aux import get_llm

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ.get("HF_API_KEY")


class Debunker:
    def __init__(self, model):
        # hamburger-style structure:
        self.heading = namedtuple("Heading", ["name", "content"])
        self.hamburger = [
            self.heading(name="Myth", content=None),
            self.heading(name="##FACT", content=None),
            self.heading(name="##MYTH", content=None),
            self.heading(name="##FALLACY", content=None),
            self.heading(name="##FACT", content=None),
        ]
        self.llm = get_llm(model)
        self.flicc_model = "fzanartu/flicc"
        self.card_model = "crarojasca/BinaryAugmentedCARDS"
        self.semantic_textual_similarity = "sentence-transformers/all-MiniLM-L6-v2"
        self.taxonomy_cards = "crarojasca/TaxonomyAugmentedCARDS"

        self.dirname = os.path.dirname(os.path.abspath("__file__"))
        self.filename = os.path.join(
            self.dirname, "src/debunker/climate_fever_cards.csv"
        )

    def generate_st_layer(self, claim, factual_information):
        # generate fact layer from fact_check input
        prompt = FACTUAL_RESPONSE
        chain = prompt | self.llm
        return chain.invoke(
            {"claim": claim, "factual_information": factual_information}
        ).content

    def generate_nd_layer(self, claim):
        ## MYTH: Summ
        prompt = SUMMARIZATION
        chain = prompt | self.llm
        return chain.invoke({"text": claim}).content

    def generate_rd_layer(self, claim):
        ## FALLACY: Fallacy

        # 1 predict fallacy label in FLICC taxonomy
        detected_fallacy = self.endpoint_query(model=self.flicc_model, payload=claim)[
            0
        ][0].get("label")
        fallacy_definition = DEFINITIONS.get(detected_fallacy)

        # 2 get all examples with the same label
        claims = FALLACY_CLAIMS.get(detected_fallacy, None)

        # 3 get cosine similarity for all claims and myth
        example_myths = self.endpoint_query(
            payload={"source_sentence": claim, "sentences": claims},
            model=self.semantic_textual_similarity,
        )

        # 3 # get most similar claim and FACT
        max_similarity = example_myths.index(max(example_myths))
        example_myth = claims[max_similarity]
        example_response = DEBUNKINGS.get(claims[max_similarity])
        fact = re.findall(r"## FALLACY:.*?(?=##)", example_response, re.DOTALL)[
            0
        ]  # get only the fallacy layer from the example.
        fact = fact.replace("## FALLACY:", "")

        prompt = INCONTEXT
        chain = prompt | self.llm
        content = chain.invoke(
            {
                "misinformation": claim,
                "detected_fallacy": detected_fallacy,
                "fallacy_definition": fallacy_definition,
                "example_response": fact,
                "example_myth": example_myth,
                "factual_information": self.hamburger[1].content,
            }
        ).content

        # content = re.sub(r"Response:", "", content)

        return content

    def generate_th_layer(self, misinformation):

        ## FACT: Concluding
        cards_label = self.endpoint_query(
            model=self.taxonomy_cards, payload=misinformation
        )[0][0].get("label")
        # 1 get all claims with same label from FEVER dataset
        claims = self.get_fever_claims(cards_label)
        prompt_completition = {"fact": self.hamburger[1].content}
        if claims:
            prompt = CONCLUDING_INCONTEXT
            example_myths = self.endpoint_query(
                payload={
                    "input": {"source_sentence": misinformation, "sentences": claims}
                },
                model=self.semantic_textual_similarity,
            )
            max_similarity = example_myths.index(max(example_myths))
            example_myth = claims[max_similarity]
            complementary_details = self.get_fever_evidence(example_myth)
            prompt_completition.update({"complementary_details": complementary_details})
        else:
            prompt = CONCLUDING

        chain = prompt | self.llm

        return chain.invoke(prompt_completition).content

    def rebuttal_generator(self, claim, factual_information):

        # generate rebuttal
        self.hamburger[0] = self.hamburger[0]._replace(content=claim)
        ## FACT
        self.hamburger[1] = self.hamburger[1]._replace(
            content=self.generate_st_layer(claim, factual_information).strip()
        )
        ## MYTH
        self.hamburger[2] = self.hamburger[2]._replace(
            content=self.generate_nd_layer(claim).strip()
        )
        ## FALLACY
        self.hamburger[3] = self.hamburger[3]._replace(
            content=self.generate_rd_layer(claim).strip()
        )
        ## FACT
        self.hamburger[4] = self.hamburger[4]._replace(
            content=self.generate_th_layer(claim).strip()
        )

        # compose and format the string
        rebuttal = f"{self.hamburger[1].name}: {self.hamburger[1].content}\n"
        rebuttal += f"{self.hamburger[2].name}: {self.hamburger[2].content}\n"
        rebuttal += f"{self.hamburger[3].name}: {self.hamburger[3].content}\n"
        rebuttal += f"{self.hamburger[4].name}: {self.hamburger[4].content}\n"

        return rebuttal

    def endpoint_query(self, payload, model):
        headers = {"Authorization": f"Bearer {os.environ['HUGGINGFACEHUB_API_TOKEN']}"}
        options = {"use_cache": False, "wait_for_model": True}
        payload = {"inputs": payload, "options": options}
        api_url = f"https://api-inference.huggingface.co/models/{model}"
        response = requests.post(api_url, headers=headers, json=payload, timeout=120)
        return json.loads(response.content.decode("utf-8"))

    def retry_on_exceptions(self, function, *args):
        attempt = 0
        while attempt < 5:
            try:
                return function(*args)
            except (KeyError, ValueError):
                print("retrying %d out of 5", attempt + 1)
                time.sleep(5 * (attempt + 1))
                attempt += 1
                continue
        # Return None if no response after five attempts
        return None

    def get_fever_claims(self, label):
        claims = []

        with open(self.filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["claim_label"] == 1 and row["CARDS_label"] == label:
                    claims.append(row["claim"])
        return claims

    def get_fever_evidence(self, claim):
        evidences = []
        with open(self.filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["claim_label"] == 1 and row["claim"] == claim:
                    for evidence_dict in literal_eval(row["evidences"]):
                        evidences.append(evidence_dict["evidence"])
        return "\n".join("* " + evidence for evidence in evidences)
