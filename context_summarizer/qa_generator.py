from transformers import pipeline

# load local text generation model
generator = pipeline("text-generation", model="gpt2")

def generate_qa(summary):

    prompt = f"""
Generate 3 questions and answers from the following text.

Text:
{summary}

Format:
Q1:
A1:
"""

    result = generator(prompt, max_length=200, num_return_sequences=1)

    return result[0]["generated_text"]


def ask_question(vector_db, question):

    docs = vector_db.similarity_search(question)

    context = docs[0].page_content

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    result = generator(prompt, max_length=150, num_return_sequences=1)

    return result[0]["generated_text"]
