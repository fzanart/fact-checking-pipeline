import logging
from .aux import parser, get_llm, clean_and_match
from .prompts import stance_detection_template, template_merge
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

logging.basicConfig(format="%(message)s", level=logging.INFO)


from transformers import pipeline
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load the pipeline once, outside of the functions
pipe = pipeline("text-classification", model="fzanartu/climate-fact-checker")


def process_evidence(claim, evidence):
    input_text = f"{claim} [SEP] {evidence}"
    result = pipe(input_text)

    # The pipeline usually returns a list of dicts, we take the first one
    return result[0]["label"]


def stance_detection(evidence_docs, claim):
    results = {}

    with ThreadPoolExecutor() as executor:
        future_to_evidence = {
            executor.submit(process_evidence, claim, evidence): i
            for i, evidence in enumerate(evidence_docs)
        }

        for future in as_completed(future_to_evidence):
            evidence_index = future_to_evidence[future]
            try:
                stance = future.result()
                results[str(evidence_index)] = stance
            except Exception as exc:
                print(f"Evidence {evidence_index} generated an exception: {exc}")

    return results


def merge_answer(model, evidence_docs, labels, claim):

    llm = get_llm(model)
    # Identify 'refutes' labels
    relevant_keys = [
        int(key) for key in labels if labels[key]["stance"].lower() == "refutes"
    ]
    # Select the corresponding documents from evidence_docs
    evidence = {
        str(k): evidence_docs[k] for k, idx in zip(relevant_keys, evidence_docs)
    }

    logging.info(f"evidence = {evidence}")

    if not evidence:

        return "No refuting evidence has been found"

    merge_prompt = PromptTemplate(
        template=template_merge, input_variables=["context", "claim"]
    )

    merge_chain = merge_prompt | llm
    answer = merge_chain.invoke({"context": evidence, "claim": claim})

    # Extract source URLs from the metadata of each document in the evidence
    source = "\n".join({doc.metadata["url"] for doc in evidence.values()})

    return answer, source
