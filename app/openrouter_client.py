from typing import Any


class OpenRouterClient:
    """Lightweight wrapper around the OpenAI client to access chat API."""

    def __init__(self, base_url: str, api_key: str):
        from openai import OpenAI  # imported here to keep imports lightweight

        self.client = OpenAI(base_url=base_url, api_key=api_key)

    @property
    def chat(self) -> Any:
        return self.client.chat
