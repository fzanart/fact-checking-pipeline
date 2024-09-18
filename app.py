"""Fact-checking pipeline and Gradio interface for claim verification. """

import logging

# import json
from src.fact_check.search import keyword_search_result, get_urls
from src.fact_check.retrieve import (
    fetch_url_and_parse_html,
    split_into_chunked_docs,
    retrieve_docs,
)
from src.fact_check.process import stance_detection, merge_answer
from src.fact_check.aux import clean_and_match, ensemble_classifier, editing_chain
from src.debunker.core import Debunker
from src.zero_shot.zero_shot import zero_shot_rebuttal

import gradio as gr

logging.basicConfig(format="%(message)s", level=logging.INFO)


def fact_checking_pipeline(claim):

    model, keyword_template = "openai", "cot"
    debunker = Debunker(model)
    logging.info("claim = %s", claim)

    # 1. Web documents retrieval:
    keywords = keyword_search_result(claim, model, keyword_template)
    logging.info("keywords = %s", keywords)
    urls = get_urls(keywords)
    html = fetch_url_and_parse_html(urls)
    chunked_docs = split_into_chunked_docs(html)

    # 2. Evidence Extraction:
    evidence_docs = retrieve_docs(chunked_docs, keywords)

    # 3. Stance Detection:
    labels = stance_detection(model, evidence_docs, claim)
    lbls = clean_and_match(labels)
    logging.info("lbls = %s", lbls)

    # 4. Claim Validation:
    answer = merge_answer(model, evidence_docs, lbls, claim)

    if isinstance(answer, tuple):
        # if tuple means the pipeline found supporting/refuting evidence
        try:
            content = answer[1].content
        except AttributeError:
            content = answer[1]

        factual_response = {
            "answer": content,
            "keywords": keywords,
            "source": answer[2],
            "stance": answer[0],
        }

    else:
        # "No supporting or refuting evidence has been found"
        content = answer
        factual_response = {
            "answer": content,
            "keywords": keywords,
            "source": "NA",
            "stance": "unknown",
        }

    # CARDS prediction
    cards_prediction = debunker.endpoint_query(
        model=debunker.card_model, payload=claim
    )[0][0].get("label")
    factual_response["cards_prediction"] = cards_prediction

    # Ensemble classifier
    ensemble_prediction = ensemble_classifier(
        factual_response["stance"], cards_prediction
    )
    factual_response["ensemble_prediction"] = ensemble_prediction

    if ensemble_prediction == "myth":
        # generate rebuttals
        rebuttal = debunker.rebuttal_generator(claim, factual_response["answer"])
        factual_response["rebuttal"] = rebuttal
        factual_response["detected_fallacy"] = debunker.detected_fallacy
        # TODO: add final review to remove glitches
        # edited_rebuttal = editing_chain(rebuttal)
        # factual_response["edited_rebuttal"] = edited_rebuttal
        # Add Zero-shot rebuttal
        zs_rebuttal = zero_shot_rebuttal(claim, model)
        factual_response["zero_shot_rebuttal"] = zs_rebuttal

    return str(factual_response)


demo = gr.Interface(fn=fact_checking_pipeline, inputs="text", outputs="text")
demo.queue().launch(debug=True)
