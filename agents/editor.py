import cohere # type: ignore
from config import COHERE_API_KEY # type: ignore

co = cohere.Client(COHERE_API_KEY)

MODEL = "command-a-03-2025"

def edit_article(article):
    prompt = f"""
Improve the following article to professional journalism standards.

Make it:
- Clear
- Grammatically correct
- Smooth and readable
- Professional tone

Article:
{article}
"""

    response = co.chat(
        model=MODEL,
        message=prompt,
        temperature=0.5,
        max_tokens=1200
    )

    return response.text.strip()