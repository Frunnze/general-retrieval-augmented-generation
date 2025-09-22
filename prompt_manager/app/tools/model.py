from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from app.tools.config import OPENROUTER_API_KEY, BASE_URL

# Locally downloaded model through Ollama
def AIModel(name : str = "qwen3:4b", temp : float = 1.0):

    llm = ChatOllama(
        model=name,
        temperature=temp,
        validate_model_on_init=True
    )

    return llm

# print(AIModel().invoke("What is AI ?").content)

def OpenRouterModel(name : str = "x-ai/grok-4-fast:free", temp : float = 1.0):

    llm = ChatOpenAI(
        model=name,
        temperature=temp,
        api_key=OPENROUTER_API_KEY,
        base_url=BASE_URL,
        default_headers={
        "HTTP-Referer": "http://localhost",   
        "X-Title": "Open Source Contribution"
        }
    )

    return llm

# print(OpenRouterModel().invoke("What is AI ?").content)