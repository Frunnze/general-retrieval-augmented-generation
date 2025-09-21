from langchain_ollama import OllamaEmbeddings
from typing import List

def OpenSourceEmbeddingsModel(name : str = "embeddinggemma:latest"):
    """Instantiate the Ollama Embeddings Model"""
    model = OllamaEmbeddings(model=name,
                             validate_model_on_init=True,
                             base_url="http://127.0.0.1:11434")
    
    return model

# # Accessing and using the model
# model = OpenSourceEmbeddingsModel()
# query = model.embed_query("Hello")
# print(query[:5])
# print("Dimensions : ", len(query))
# print("Type : ", type(query))