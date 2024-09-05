"""Fact-checking pipeline and Gradio interface for claim verification."""

import logging

# import json
from src.fact_check.search import keyword_search_result, get_urls
from src.fact_check.retrieve import (
    fetch_url_and_parse_html,
    split_into_chunked_docs,
    retrieve_docs,
)
from src.fact_check.process import stance_detection, merge_answer
from src.fact_check.aux import clean_and_match
from src.debunker.core import Debunker
import gradio as gr

logging.basicConfig(format="%(message)s", level=logging.INFO)


def fact_checking_pipeline(claim):

    model, keyword_template = "openai", "cot"
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
    logging.info("labels = %s", labels)
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
            "stance": "Unknown",
        }

    if factual_response["stance"] == "refutes":
        # if refutes, then generate rebuttal
        debunker = Debunker(model)
        rebuttal = debunker.rebuttal_generator(claim, factual_response["answer"])
        factual_response["rebuttal"] = rebuttal

    return str(factual_response)


demo = gr.Interface(fn=fact_checking_pipeline, inputs="text", outputs="text")
demo.queue().launch(debug=True)
