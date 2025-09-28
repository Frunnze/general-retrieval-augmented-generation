import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"D:\Project\general-retrieval-augmented-generation\prompt_manager\app\tools\.env")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL")

# print(OPENROUTER_API_KEY)
# print(BASE_URL)