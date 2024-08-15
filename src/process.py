import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
import logging
from .aux import parser, get_llm, clean_and_match
from .prompts import stance_detection_template, template_merge
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

logging.basicConfig(format="%(message)s", level=logging.INFO)


from transformers import AutoTokenizer, pipeline
from concurrent.futures import ThreadPoolExecutor, as_completed

tokenizer = AutoTokenizer.from_pretrained("fzanartu/climate-fact-checker")
pipe = pipeline(
    "text-classification", model="fzanartu/climate-fact-checker", tokenizer=tokenizer
)


def process_evidence(claim, evidence):
    max_length = 500

    # Tokenize claim and evidence separately
    claim_tokens = tokenizer.tokenize(claim)
    evidence_tokens = tokenizer.tokenize(evidence)
    print(len(claim_tokens) + len(evidence_tokens))

    # Determine the split between claim and evidence
    half_tokens = max_length // 2

    if len(claim_tokens) + len(evidence_tokens) > max_length:

        # If they exceed the limit, truncate them proportionally
        claim_tokens = claim_tokens[:half_tokens]
        evidence_tokens = evidence_tokens[: max_length - len(claim_tokens)]

    # Reconstruct the input text
    truncated_claim = tokenizer.convert_tokens_to_string(claim_tokens)
    truncated_evidence = tokenizer.convert_tokens_to_string(evidence_tokens)

    input_text = f"{truncated_claim} [SEP] {truncated_evidence}"

    print(input_text)

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
