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
