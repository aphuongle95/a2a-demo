import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

try:
    response = model.generate_content("Explain how AI works in a few words")
    print('Wohoo! Setup complete!\n\nWe are good to go!')
    print(f'Response: {response.text}')
except Exception as e:
    print(f'Error verifying Google API key: {e}')
