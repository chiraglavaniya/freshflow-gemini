import os

import google.generativeai as genai


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")


def generate_insight(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response")

    return text.strip()
