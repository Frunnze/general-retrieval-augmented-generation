from fastapi import FastAPI
# from openai import OpenAI
from app.tools.model import OpenRouterModel
from dotenv import load_dotenv
import os
import chromadb


load_dotenv()
openai = OpenRouterModel()
chromadb = chromadb.PersistentClient()
topics_col = chromadb.get_or_create_collection("topics")

def create_app():
    app = FastAPI()

    # Register the routes
    from .apis.ai_res import ai_res_router
    app.include_router(ai_res_router)

    from .apis.topics import topics_router
    app.include_router(topics_router)

    from .apis.material import materials_router
    app.include_router(materials_router)

    return app