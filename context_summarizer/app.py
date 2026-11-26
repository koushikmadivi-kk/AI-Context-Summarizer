from flask import Flask, request, jsonify, render_template
from pdf_loader import load_pdf
from summarizer import process_documents, generate_summary
from qa_generator import generate_qa, ask_question
import os
import uuid

app = Flask(__name__)

# store vector database globally
vector_db = None


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# TEXT SUMMARIZATION
# -------------------------
@app.route("/summarize_text", methods=["POST"])
def summarize_text():

    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Text is required"}), 400

        text = data["text"]

        summary = generate_summary(text)

        qa = generate_qa(summary)

        return jsonify({
            "status": "success",
            "summary": summary,
            "qa": qa
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# -------------------------
# PDF SUMMARIZATION
# -------------------------
@app.route("/summarize_pdf", methods=["POST"])
def summarize_pdf():

    global vector_db

    try:

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # create unique file name
        filename = str(uuid.uuid4()) + ".pdf"
        path = os.path.join("uploads", filename)

        os.makedirs("uploads", exist_ok=True)

        file.save(path)

        # load pdf
        documents = load_pdf(path)

        # process document
        chunks, vector_db = process_documents(documents)

        # generate summary
        summary = generate_summary(chunks)

        # generate Q&A
        qa = generate_qa(summary)

        # remove file after processing
        os.remove(path)

        return jsonify({
            "status": "success",
            "summary": summary,
            "qa": qa
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# -------------------------
# ASK QUESTION
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():

    global vector_db

    try:

        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "Question required"}), 400

        question = data["question"]

        if vector_db is None:
            return jsonify({"error": "Upload a document first"}), 400

        answer = ask_question(vector_db, question)

        return jsonify({
            "status": "success",
            "answer": answer
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
