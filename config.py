import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GOOGLE_API_KEY or not HUGGINGFACE_API_TOKEN or not GEMINI_API_KEY:
    raise ValueError("One or more environment variables are not set.")
