from fastapi import APIRouter, UploadFile, File
import uuid
import PyPDF2
from io import BytesIO

from ..tools.chroma import embed_text
from .. import topics_col


materials_router = APIRouter()

def extract_pdf_text(pdf_bytes):
    reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

@materials_router.post("/add_material")
async def add_material(topic: str, file: UploadFile = File(...)):
    try:
        # Read file content
        content = await file.read()
        text = content.decode(errors="replace")

        # If the file is a PDF, extract text using PyPDF2
        if file.filename.endswith(".pdf"):
            text = extract_pdf_text(content)

        # Create chunks
        words = text.split()
        chunks = []
        for i in range(0, len(words), 350):
            chunks.append(" ".join(words[i:i+350]))

        # Embed text
        embeddings = embed_text(chunks)

        # Save to db
        topics_col.add(
            ids=[str(uuid.uuid4()) for _ in range(len(embeddings))],
            documents=chunks,
            embeddings=embeddings,
            metadatas=[{"topic": topic} for _ in range(len(embeddings))]
        )

        return {"msg": "Materials were added!"}
    except Exception as e:
        print(e)
        return {"msg": "Server Error"}, 500
    

@materials_router.get("/materials")
async def get_materials():
    try:
        # Query all documents in the topics collection
        results = topics_col.get()
        # Return documents and metadata
        ids = results.get("ids", [])
        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])
        # Build a list of document objects
        docs = [
            {
                "id": ids[i],
                "document": documents[i],
                "metadata": metadatas[i]
            }
            for i in range(len(documents))
        ]
        return docs
    except Exception as e:
        print(e)
        return {"msg": "Server Error"}, 500