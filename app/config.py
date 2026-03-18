import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")