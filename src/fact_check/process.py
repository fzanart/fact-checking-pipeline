"""Module for processing stance detection and merging answers."""

import logging
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain.callbacks.tracers import ConsoleCallbackHandler
from .aux import parser, get_llm
from .prompts import stance_detection_template, template_merge

logging.basicConfig(format="%(message)s", level=logging.INFO)


def stance_detection(model, evidence_docs, claim):
    # Get the language model
    llm = get_llm(model)

    # Initialize an empty dictionary to store chains
    chains_dict = {}

    # Iterate through each chunk of evidence
    for i, chunk in enumerate(evidence_docs):
        # Create a prompt template for stance detection
        prompt = PromptTemplate(
            template=stance_detection_template,
            input_variables=["claim"],
            partial_variables={
                "evidence": chunk,
                "format_instructions": parser.get_format_instructions(),
            },
        )
        # Dynamically name the chains based on their index
        chain_name = str(i)
        # Combine prompt with language model and add to chains dictionary
        chains_dict[chain_name] = prompt | llm

    # Create a parallel runnable from the chains dictionary
    map_chain = RunnableParallel(**chains_dict)

    # Invoke the parallel chain with the claim and get labels
    labels = map_chain.invoke({"claim": claim})

    return labels


def merge_answer(model, evidence_docs, labels, claim):
    llm = get_llm(model)

    # Identify 'refutes' and 'support' labels
    refutes_keys = [
        int(key) for key in labels if labels[key]["stance"].lower() == "refutes"
    ]
    support_keys = [
        int(key) for key in labels if labels[key]["stance"].lower() == "support"
    ]

    # Determine the stance and relevant keys
    if support_keys:
        stance = "support"
        relevant_keys = support_keys
    elif refutes_keys:
        stance = "refutes"
        relevant_keys = refutes_keys
    else:
        return "No supporting or refuting evidence has been found"

    # Select the corresponding documents from evidence_docs
    evidence = {
        str(k): evidence_docs[k] for k, idx in zip(relevant_keys, evidence_docs)
    }

    logging.info("evidence = %s", evidence)

    merge_prompt = PromptTemplate(
        template=template_merge, input_variables=["stance", "context", "claim"]
    )

    merge_chain = merge_prompt | llm
    answer = merge_chain.invoke(
        {"stance": stance, "context": evidence, "claim": claim},
        config={"callbacks": [ConsoleCallbackHandler()]},
    )

    # Extract source URLs from the metadata of each document in the evidence
    source = "\n".join({doc.metadata["url"] for doc in evidence.values()})

    return stance, answer, source
