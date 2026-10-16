from ollama import embeddings
from app.config import EMBEDDING_MODEL


def get_embedding(text: str) -> list[float]:
    response = embeddings(
        model=EMBEDDING_MODEL,
        prompt=text,
    )
    return response["embedding"]
