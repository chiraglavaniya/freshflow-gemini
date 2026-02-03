import google.generativeai as genai
import os

def init_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_insight(prompt):
    model = genai.GenerativeModel("gemini-pro")
    return model.generate_content(prompt).text
