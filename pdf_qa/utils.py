import streamlit as st

def show_spinner(func):
    """
    Decorator to show a spinner in Streamlit during function execution.
    """
    def wrapper(*args, **kwargs):
        with st.spinner("Processing..."):
            return func(*args, **kwargs)
    return wrapper
