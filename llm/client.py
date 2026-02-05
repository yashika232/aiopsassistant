import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# The modern client defaults to the stable v1 API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(system_prompt: str, user_prompt: str) -> str:
    # 'gemini-1.5-flash' is fully supported here
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=user_prompt,
        config={'system_instruction': system_prompt}
    )
    return response.text.strip()