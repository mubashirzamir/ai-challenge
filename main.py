import streamlit as st
from app.config import load_config
from app.openrouter_client import OpenRouterClient
from app.prompts import PromptGenerator
from app.reviewer import CodeReviewer

# =========================
# CONFIG & INITIALIZATION
# =========================

config = load_config()

OPENROUTER_BASE_URL = config.openrouter_base_url
OPENROUTER_API_KEY = config.openrouter_api_key
OPENROUTER_MODEL = config.openrouter_model
APP_URL = config.app_url
APP_TITLE = config.app_title

if not OPENROUTER_BASE_URL or not OPENROUTER_API_KEY:
    st.error("Missing OpenRouter credentials. Please set OPENROUTER_BASE_URL and OPENROUTER_API_KEY in .env")
    st.stop()

client = OpenRouterClient(OPENROUTER_BASE_URL, OPENROUTER_API_KEY)

# =========================
# SINGLE RESPONSIBILITY: AI Reviewer
# =========================
reviewer = CodeReviewer(client, OPENROUTER_MODEL, APP_URL, APP_TITLE)

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(page_title="Smart Code Reviewer", layout="wide")
st.title("Smart Code Reviewer by Mubashir Zamir")
st.write("Analyze your code for readability, structure, and maintainability.")

# Sidebar
st.sidebar.header("Settings")
language = st.sidebar.selectbox("Programming Language", ["Python", "JavaScript", "Java", "C++", "Other"])
strict_mode = st.sidebar.toggle("Strict Mode")
use_streaming = st.sidebar.checkbox("Use Streaming Output", value=False)

# Code input
code_input = st.text_area("Paste your code here:", height=300)

# Button action
if st.button("Review Code"):
    if not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                prompt = PromptGenerator.generate(code_input, language, strict_mode)

                if use_streaming:
                    st.subheader("📋 Review Results (Streaming)")
                    output_placeholder = st.empty()
                    output_text = ""
                    for chunk in reviewer.review_stream(prompt):
                        output_text += chunk
                        output_placeholder.markdown(output_text)
                else:
                    result = reviewer.review(prompt)
                    st.subheader("📋 Review Results")
                    st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Built as a Smart Code Reviewer AI prototype using OpenRouter")
