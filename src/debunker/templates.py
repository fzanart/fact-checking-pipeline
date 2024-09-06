"""
Contains prompt templates to be used on app.py
"""

from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

FACTUAL_RESPONSE = PromptTemplate.from_template(
    """Based on the provided claim and factual information, generate a factual response in two sentences (or fewer than 30 words). 
claim: {claim}
factual_information: {factual_information}
response: """
)

UNKNOWN_FACT = PromptTemplate.from_template(
    """You are an expert climate analyst tasked with providing precise and concise responses to climate change misinformation
Generate a factual response in two sentences (or fewer than 30 words). Offer clear, memorable alternatives to counter the misinformation. 
For example: "Arctic sea ice dropped 40% since the '70s, hitting record lows." Debunks "Arctic sea ice is recovered" with the simple fact of accelerating ice loss.
misinformation: {claim}
response: """
)

INCONTEXT = [
    (
        "system",
        "You are a senior climate analyst, an expert in identifying and responding to climate change misinformation.",
    ),
    (
        "human",
        "What fallacy is contained in the following climate change misinformation?\nmisinformation: {misinformation}",
    ),
    (
        "ai",
        "Your text contains {detected_fallacy} fallacy. {detected_fallacy} fallacy is {fallacy_definition}",
    ),
    (
        "human",
        "What is the factual evidence surrounding this climate change misinformation?",
    ),
    ("ai", "{factual_information}"),
    (
        "human",
        "Provide a precise and concise response to this climate change misinformation. In two sentences, explicitly name the fallacy, explain why it's incorrect, and link it to factual evidence showing how it distorts reality. Consider the following example before providing your answer: Misinformation: {example_myth}",
    ),
    ("ai, Response: {example_response}"),
    ("human", "Misinformation: {misinformation}"),
]

SUMMARIZATION = PromptTemplate.from_template(
    """[INST]
You are a paraphrasing system capable of providing rephrased versions of texts in clear and concise language.
Paraphrase the following text in 30 words or fewer. Only refer to the text without adding additional elements or opinions.
[/INST]

text: {text}
Summary: 
"""
)

CONCLUDING = PromptTemplate.from_template(
    """<s>[INST] 1. Reinforce the following fact and provide complementary details, if relevant, to enhance understanding.
2. The output should be simple text summarizing the information in 30 words or fewer. [/INST]
</s>
# Fact:
{fact}
# Summary:
"""
)

CONCLUDING_INCONTEXT = PromptTemplate.from_template(
    """<s>[INST] 1. Reinforce the following fact and provide complementary details, if relevant, to enhance understanding.
2. The output should be simple text summarizing the information in 30 words or fewer. Replace technical and complex words with simpler synonyms and delete unimportant information.[/INST]
Complementary details:
{complementary_details}
</s>

# Fact:
{fact}
# Summary:
"""
)
