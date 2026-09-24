import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=API_KEY) if API_KEY else None


def ask_model(question: str) -> str | None:
    if client is None:
        return None
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful student budgeting assistant."},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as error:
        return f"Model request failed: {error}"