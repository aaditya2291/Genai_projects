import os
from dotenv import load_dotenv

load_dotenv()

groq = os.getenv("groq_api_key")
model_name = os.getenv("llama-3.1-8b-instant")
