from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEBSITE_URL = "https://www.islamveihsan.com/" 