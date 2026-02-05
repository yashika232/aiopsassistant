import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def call_llm(system_prompt: str, user_prompt: str) -> str:
    prompt = f"""
{system_prompt}

User Input:
{user_prompt}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
