# 📄 PDF Q&A Chatbot

This app lets you upload a PDF file and ask questions about it using natural language. It uses semantic search with FAISS and answers using a T5-based model.

## 🧠 Features

- Upload any PDF
- Ask informal/misspelled questions
- See multi-turn chat history
- Lightweight, runs locally
- Fast: FLAN-T5 & MiniLM

## 🚀 How to Run

```bash
cd pdf_qa_chatbot
pip install -r requirements.txt
streamlit run app.py

---

## 💡 Future Ideas
-Deploy on Hugging Face Spaces

-Add user login / access control

-Save history to disk


---

### 📁 `pdf_qa_chatbot/.gitignore`

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.venv
llm-env/
*.pdf
.DS_Store
