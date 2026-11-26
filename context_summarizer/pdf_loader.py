import pdfplumber
from langchain_core.documents import Document

def load_pdf(file_path):

    documents = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={"page": page.page_number}
                    )
                )

    return documents
