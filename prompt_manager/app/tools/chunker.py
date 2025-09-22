from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def get_chunks(text : str, chunkSize : int = 600, chunkOverlap : int = 100):
    textSplitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", '\n', " "],
        chunk_size = chunkSize,
        chunk_overlap = chunkOverlap
    )

    splitText = textSplitter.split_text(text)

    return splitText