import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# =========================
# CONFIG & INITIALIZATION
# =========================

load_dotenv()

OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")  # default if not set
APP_URL = os.getenv("APP_URL", "http://localhost:8501")
APP_TITLE = os.getenv("APP_TITLE", "Smart Code Reviewer")

if not OPENROUTER_BASE_URL or not OPENROUTER_API_KEY:
    st.error("Missing OpenRouter credentials. Please set OPENROUTER_BASE_URL and OPENROUTER_API_KEY in .env")
    st.stop()

client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=OPENROUTER_API_KEY)

# =========================
# SINGLE RESPONSIBILITY: Prompt Generator
# =========================
class PromptGenerator:
    @staticmethod
    def generate(code: str, language: str, strict: bool) -> str:
        mode_text = "Be strict and critical." if strict else "Be balanced and constructive."
        return f"""
You are a senior software engineer performing a professional code review.

Language: {language}

{mode_text}

Evaluate the code for:
1. Readability
2. Structure
3. Maintainability

Return your response in the following format:

### Issues
- (List 3 clear problems)

### Improvements
- (List 3 actionable improvements)

### Positive Note
- (Mention 1 good aspect)

### Refactored Code (optional)
(Provide improved version if applicable)

### Score
(Give a score out of 10)

Code:
{code}
"""

# =========================
# SINGLE RESPONSIBILITY: AI Reviewer
# =========================
class CodeReviewer:
    def __init__(self, client: OpenAI, model: str, app_url: str, app_title: str):
        self.client = client
        self.model = model
        self.extra_headers = {"HTTP-Referer": app_url, "X-Title": app_title}

    def review(self, prompt: str) -> str:
        """Non-streaming completion"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert code reviewer."},
                {"role": "user", "content": prompt},
            ],
            extra_headers=self.extra_headers,
        )
        return response.choices[0].message.content

    def review_stream(self, prompt: str):
        """Streaming completion (generator)"""
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert code reviewer."},
                {"role": "user", "content": prompt},
            ],
            stream=True,
            extra_headers=self.extra_headers,
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            yield chunk.choices[0].delta.content

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