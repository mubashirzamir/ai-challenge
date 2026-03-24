# Smart Code Reviewer AI

[Placeholder Link](#)  

A Streamlit prototype that uses OpenRouter to review code for readability, structure, and maintainability. Paste your code, select the programming language, toggle strict mode, and get a professional review along with suggested improvements and a positive note. Streaming output is also supported.  

## Setup

1. **Clone the repo**  
```bash
git clone <repo-url>
cd ai-challenge
````

2. **Install dependencies with Poetry**

```bash
poetry install
poetry shell
```

3. **Create a `.env` file** in the project root:

```env
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=sk-xxxxxx
OPENROUTER_MODEL=nvidia/nemotron-3-super-120b-a12b:free
APP_URL=http://localhost:8501
APP_TITLE=Smart Code Reviewer
```

4. **Run the app**

```bash
streamlit run app/app.py
```

## Usage

* Paste your code in the text area
* Select the programming language and toggle strict mode
* Optionally enable streaming output
* Click **Review Code** to get AI feedback

## Notes

* Requires a valid OpenRouter API key
* Default model is `nvidia/nemotron-3-super-120b-a12b:free` if not specified in `.env`
* Designed for demo and prototype purposes