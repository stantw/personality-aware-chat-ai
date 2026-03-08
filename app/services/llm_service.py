from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text(user_input: str, model: str = "gemini-3-flash-preview") -> str:
    response = client.models.generate_content(
        model=model,
        contents=user_input
    )
    return response.text