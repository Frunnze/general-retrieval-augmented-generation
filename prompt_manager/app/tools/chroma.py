from .. import topics_col
from .. import openai


def embed_text(strs: list):
    res = openai.embeddings.create(
        input=strs,
        model="text-embedding-3-small"
    )
    return [item.embedding for item in res.data]

def get_context(topics, text):
    embeddings = embed_text([text])
    results = topics_col.query(
        query_embeddings=embeddings,
        n_results=2,
        where={"topic": {"$in": topics}}
    )
    print("get_context", results["documents"])
    return results["documents"]