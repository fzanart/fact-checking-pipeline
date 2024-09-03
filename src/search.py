"""Module for performing keyword searches and retrieving URLs."""

import re
from .aux import get_llm
from .prompts import (
    zero_shot_retrieval_template,
    few_shot_retrieval_template,
    cot_retrieval_template,
)
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.prompts import PromptTemplate

prompts = {
    "zero_shot": zero_shot_retrieval_template,
    "few_shot": few_shot_retrieval_template,
    "cot": cot_retrieval_template,
}


def keyword_search_result(statement, model, prompt_template):

    llm = get_llm(model)
    prompt = PromptTemplate(
        template=prompts.get(prompt_template), input_variables=["statement"]
    )
    chain = prompt | llm
    keywords = chain.invoke({"statement": statement})

    if prompt_template == "cot":

        try:
            content = keywords.content
        except AttributeError:
            content = keywords

        kw = re.findall(r"(?<=The keyword search could be:\s).*", content)
        if kw:
            return kw[0]

    return content


def get_urls(keywords):

    search = DuckDuckGoSearchResults()

    white_list = [
        "climate.gov",
        "climate.nasa.gov",
        "climatechangeinaustralia.gov.au",
        "climatefeedback.org",
        "globalchange.gov",
        "ipcc.ch",
        "nationalacademies.org",
        "news.climate.columbia.edu",
        "noaa.gov",
        "nsidc.org",
        "realclimate.org",
        "royalsociety.org",
        "skepticalscience.com",
        "unfccc.int",
        "wmo.int",
    ]

    search_query = keywords + " " + " OR ".join(["site:" + site for site in white_list])

    results = search.run(search_query)
    urls = re.findall(r"link: ([^\]]+)", results)

    return urls
