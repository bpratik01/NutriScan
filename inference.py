import requests
import os
from dotenv import find_dotenv, load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Configure API keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

HUGGINGFACE_API_TOKEN = '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'
GEMIONI_API_KEY = 'AIzaSyDE7plTxouTUdJPLFrQxFHq3h_Rq0E8CVg'
os.environ['GEMIONI_API_KEY'] = GEMIONI_API_KEY
model = genai.GenerativeModel('gemini-pro')

# Function to extract text from image using Hugging Face Inference API
def img2text(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    
    # Make request to Hugging Face Inference API
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/octet-stream"
    }
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    
    if response.status_code == 200:
        result = response.json()
        text = result[0]['generated_text']
        print("Image Description:", text)

        prompt = "You are a nutritionist and you are expected to give nutrient values for the following food description: " + text
        response = model.generate_content(prompt)

        print("Full Response:", response)

        try:
            nutrient_values = response.candidates[0].content.parts[0].text
            print("Nutrient Values:", nutrient_values)
            return text, nutrient_values, response
        except AttributeError as e:
            print(f"AttributeError: {e}")
            print("Response Attributes:", dir(response))
            return text, "Error extracting nutrient values", response
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return "Error", response.status_code, response.json()

