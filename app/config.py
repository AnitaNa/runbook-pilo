import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.postgres_url = os.getenv("POSTGRES_CONNECTION_STRING")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a single global instance to import across our app
settings = Settings()