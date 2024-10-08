"""Module for fetching, parsing, and retrieving web content using LangChain and Chroma."""

import os
import html2text
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings


# Fetch
def fetch_url_and_parse_html(source_url):
    if not isinstance(source_url, list):
        source_url = [source_url]
    # Initialize the loader with the URL and load the HTML content asynchronously
    loader = AsyncChromiumLoader(source_url)
    html = loader.load()

    # return html docs that doesnt startswith Error, e.g.: TimeoutError
    # add url to Document class for trasability
    documents = []
    for document, url in zip(html, source_url):
        if not document.page_content.startswith("Error:"):
            document.metadata = {"url": url}
            # Parse html, convert to text
            document.page_content = parse_html(document.page_content)
            documents.append(document)

    if not documents:
        raise ValueError(
            "Failed to fetch and parse HTML content for all provided URLs."
        )

    return documents


# Parse
def parse_html(document):
    # Initialize the HTML to text converter
    h = html2text.HTML2Text()
    h.ignore_links = True
    # Convert the HTML content to text
    text_content = h.handle(document)
    return text_content


# Split
def split_into_chunked_docs(documents, chunk_size=512):
    if not isinstance(documents, list):
        documents = [documents]

    # Initialize a text splitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=chunk_size, chunk_overlap=0
    )
    # Split the text content
    chunked_docs = text_splitter.split_documents(documents)

    return chunked_docs


# RAG
def retrieve_docs(
    chunked_docs, keywords, model_name="sentence-transformers/all-MiniLM-l6-v2"
):
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.environ.get("HF_API_KEY"),
        model_name=model_name,
    )

    vectorstore = Chroma.from_documents(
        chunked_docs,
        embedding=embeddings,
    )

    doc = vectorstore.similarity_search(keywords)

    return doc
