import cohere # type: ignore
from config import COHERE_API_KEY # type: ignore

co = cohere.Client(COHERE_API_KEY)

MODEL = "command-a-03-2025"

def write_article(topic, content):
    prompt = f"""
You are a professional journalist.

Write a high-quality article on: {topic}

Based on this research:
{content}

Requirements:
- Clear introduction
- Well-structured paragraphs
- Simple and engaging language
- No repetition
- Strong conclusion
"""

    response = co.chat(
        model=MODEL,
        message=prompt,
        temperature=0.7,
        max_tokens=1200
    )

    return response.text.strip()


def generate_headline(article):
    response = co.chat(
        model=MODEL,
        message=f"Generate a catchy news headline for:\n{article}",
        temperature=0.7,
        max_tokens=50
    )

    return response.text.strip()