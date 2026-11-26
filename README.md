# AI Context Summarizer

An AI-powered application built using Python and Flask that summarizes text and PDF documents, generates questions and answers from summaries, and supports context-based question answering using semantic document retrieval.

## Overview

The AI Context Summarizer is designed to make reading and understanding lengthy documents easier. It uses Natural Language Processing (NLP), Transformer-based language models, and semantic search techniques to extract important information and generate concise summaries.

Users can provide text or upload PDF documents for processing. The application generates summaries and automatically produces questions and answers based on the summarized content.

## Features

- **Text Summarization:** Converts lengthy text into concise and meaningful summaries.
- **PDF Processing:** Extracts text from PDF documents using PDFPlumber.
- **AI-Powered Summarization:** Uses Hugging Face Transformer models for text summarization.
- **Automatic Q&A Generation:** Generates three questions and answers from the generated summary.
- **Semantic Search:** Uses vector embeddings and FAISS for document similarity search.
- **Context-Based Question Answering:** Retrieves relevant document content to support question answering.
- **Web Interface:** Provides a simple interface built using HTML, CSS and JavaScript.

## Technologies Used

### Programming Language
- Python

### Backend
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### AI & Language Models
- Google FLAN-T5 Base – Text summarization
- GPT-2 – Text generation for question and answer generation
- Sentence Transformers (all-MiniLM-L6-v2) – Text embeddings

### Frameworks & Libraries
- Hugging Face Transformers
- LangChain
- FAISS
- PDFPlumber

## System Architecture

1. **Input:** User provides text or uploads a PDF document.
2. **Text Extraction:** PDFPlumber extracts text from uploaded PDF files.
3. **Text Chunking:** LangChain splits documents into smaller chunks.
4. **Embedding Generation:** Sentence Transformers converts text chunks into vector embeddings.
5. **Vector Storage:** FAISS stores embeddings for similarity-based retrieval.
6. **Summarization:** FLAN-T5 Base generates a concise summary.
7. **Q&A Generation:** GPT-2 generates questions and answers from the summary.
8. **Question Answering:** Relevant document content is retrieved through semantic similarity search and passed to GPT-2.

## Project Structure

```text
AI-Context-Summarizer/
│
├── app.py
├── summarizer.py
├── qa_generator.py
├── pdf_loader.py
│
├── templates/
│   └── index.html
│
└── uploads/
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd context_summarizer
```

### 3. Install Required Libraries

```bash
pip install flask
pip install transformers
pip install torch
pip install pdfplumber
pip install langchain
pip install langchain-community
pip install langchain-core
pip install langchain-text-splitters
pip install langchain-huggingface
pip install sentence-transformers
pip install faiss-cpu
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

## Applications

- Academic document summarization
- Research paper understanding
- Quick analysis of lengthy text
- PDF content extraction
- Automated question generation
- Document-based information retrieval

## Future Enhancements

- Improve the accuracy of generated summaries.
- Add support for multiple document formats.
- Develop an interactive chatbot interface.
- Improve context-aware question answering.
- Add document download and summary export functionality.
- Enhance the user interface and user experience.

## Author

**Madivi Sai Naga Kousikh**

B.Tech – Computer Science Engineering

GitHub: https://github.com/koushikmadivi-kk

LinkedIn: https://www.linkedin.com/in/madivi-sai-naga-kousikh-1b691135a

## License

This project is developed for educational and learning purposes.
