"""Fact-checking pipeline and Gradio interface for claim verification."""

import logging
from src.search import keyword_search_result, get_urls
from src.retrieve import (
    fetch_url_and_parse_html,
    split_into_chunked_docs,
    retrieve_docs,
)
from src.process import stance_detection, merge_answer
from src.aux import clean_and_match
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
    lbls = clean_and_match(labels)

    # 4. Claim Validation:
    answer = merge_answer(model, evidence_docs, lbls, claim)

    if isinstance(answer, tuple):
        try:
            content = answer[1].content
        except AttributeError:
            content = answer[1]

        return str(
            {
                "answer": content,
                "keywords": keywords,
                "source": answer[2],
                "stance": answer[0],
            }
        )
    return str(
        {
            "answer": answer,
            "keywords": keywords,
            "source": "NA",
            "stance": "Unknown",
        }
    )


demo = gr.Interface(fn=fact_checking_pipeline, inputs="text", outputs="text")
demo.queue().launch(debug=True)
