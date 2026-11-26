from transformers import pipeline
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# -------------------------
# Load model once
# -------------------------
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


# -------------------------
# PROCESS DOCUMENTS
# -------------------------
def process_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)

    return chunks, vector_db


# -------------------------
# GENERATE SUMMARY
# -------------------------
def generate_summary(data):

    # If input comes from PDF chunks
    if isinstance(data, list):
        text = " ".join([doc.page_content for doc in text])

    # If input is raw text
    else:
        text = data

    # Limit input size (model limit)
    text = text[:2000]

    result = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return result[0]["summary_text"]
