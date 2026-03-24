# Smart Code Reviewer AI

[Placeholder Link](#)  

A Streamlit prototype that uses OpenRouter to review code for readability, structure, and maintainability. Paste your code, select the programming language, toggle strict mode, and get a professional review along with suggested improvements and a positive note. Streaming output is also supported.  



## Setup

1. **Clone the repo**  
```bash
git clone <repo-url>
cd ai-challenge
````

2. **Create a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Create a `.env` file** in the project root:

```env
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=sk-xxxxxx
OPENROUTER_MODEL=openai/gpt-4o-mini
APP_URL=http://localhost:8501
APP_TITLE=Smart Code Reviewer
```

4. **Run the app**

```bash
streamlit run app/app.py
```

## Usage

* Paste your code in the text area
* Select language and toggle strict mode
* Click **Review Code** to get feedback

## Notes

* Requires a valid OpenRouter API key
* Default model is `gpt-3.5-turbo` if not specified in `.env`
* Designed for demo and prototype purposes