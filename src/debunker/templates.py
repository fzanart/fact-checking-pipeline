"""
Contains prompt templates to be used on app.py
"""

from langchain.prompts import PromptTemplate

FACTUAL_RESPONSE = PromptTemplate.from_template(
    """Based on the provided claim and factual information, generate a factual response in two sentences (or fewer than 30 words). 
claim: {claim}
factual_information: {factual_information}
response: """
)

INCONTEXT = PromptTemplate.from_template(
    """<s>[INST] <<SYS>>
You are a senior climate analyst, an expert in identifying and responding to climate change misinformation.
<</SYS>>
What fallacy is contained in the following climate change misinformation?
misinformation: {misinformation} [/INST] 
Your text contains {detected_fallacy} fallacy. {detected_fallacy} fallacy is {fallacy_definition} </s>
<s>[INST] What is the factual evidence surrounding this climate change misinformation?[/INST]
{factual_information}</s>
<s>[INST] Provide a precise and concise response to this climate change misinformation.
In two sentences, explicitly name the fallacy, explain why it's incorrect, and link it to factual evidence showing how it distorts reality.
Consider the following example before providing your answer:
Misinformation: {example_myth}
Response: {example_response}
Misinformation: {misinformation}
Response: 
[/INST]"""
)

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
