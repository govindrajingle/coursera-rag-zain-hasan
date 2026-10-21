import ollama
import numpy as np

from chunker import create_chunks
from pdf_reader import read_pdf

MODEL_NAME = "nomic-embed-text"

def get_embeddings(text):
    """generate an embedding verctor of a text string"""
    response = ollama.embed(
        model = MODEL_NAME,
        input = text
    )
    return np.array(response["embeddings"][0], dtype=np.float32)

def embed_chunks(chunks):
    """generate and attach an embedding to every chunk"""
    embedded_chunks = []
    for index, chunk in enumerate(chunks, start = 1):
        embedding = get_embeddings(chunk["text"])
        embedded_chunks.append({
            **chunk,
            "embedding": embedding
        })
        if index % 10 == 0 or index == len(chunks):
            print(f"embedded {index}/{len(chunks)} chunks")
    return embedded_chunks

if __name__ == "__main__":
    pages = read_pdf("test.pdf")
    chunks = create_chunks(pages)
    print(f"total chunks: {len(chunks)}")
    if not chunks:
        raise ValueError("no chunks found. Check pdf_reader.py and chunker.py")
    embedded_chunks = embed_chunks(chunks)
    first_embedding = embedded_chunks[0]["embedding"]
    print("\nembedding completed")
    print(f"embedding dimensions: {first_embedding.shape}")
    print(f"first 10 values: {first_embedding[:10]}")
    print(f"total embedded chunks: {len(embedded_chunks)}")