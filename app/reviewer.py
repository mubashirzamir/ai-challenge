class CodeReviewer:
    def __init__(self, client, model: str, app_url: str, app_title: str):
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
