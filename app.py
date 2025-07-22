import streamlit as st
from pdf_qa.pdf_processing import pdf_to_text
from pdf_qa.text_chunking import chunk_text
from pdf_qa.embedding import embed_chunks, build_faiss_index, retrieve_relevant_chunks
from pdf_qa.qa_generation import generate_answer

st.set_page_config(page_title="📄 PDF Q&A Chatbot", layout="wide")

# Session memory for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("📄 Ask Questions About Your PDF")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading PDF..."):
        text = pdf_to_text(uploaded_file)
        chunks = chunk_text(text)
        model, embeddings = embed_chunks(chunks)
        index = build_faiss_index(embeddings)

    st.success("PDF processed successfully. You can now ask questions.")

    query = st.text_input("Ask a question:", placeholder="e.g., What are the results?")
    if st.button("Get Answer") and query:
        with st.spinner("Generating answer..."):
            top_chunks = retrieve_relevant_chunks(query, chunks, model, index)
            context = "\n".join(top_chunks)
            answer = generate_answer(context, query)

            if not answer.strip():
                answer = "❌ Sorry, I couldn't find a relevant answer."

            st.session_state.chat_history.append((query, answer))

    if st.session_state.chat_history:
        st.subheader("🧠 Chat History")
        for i, (q, a) in enumerate(st.session_state.chat_history[::-1]):
            st.markdown(f"**Q{i+1}: {q}**")
            st.markdown(f"➡️ {a}")
