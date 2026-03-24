import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class AppConfig:
    openrouter_base_url: str
    openrouter_api_key: str
    openrouter_model: str
    app_url: str
    app_title: str


def load_config() -> AppConfig:
    # Load environment variables from .env if present
    load_dotenv()

    openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
    app_url = os.getenv("APP_URL", "http://localhost:8501")
    app_title = os.getenv("APP_TITLE", "Smart Code Reviewer")

    return AppConfig(
        openrouter_base_url,
        openrouter_api_key,
        openrouter_model,
        app_url,
        app_title,
    )
