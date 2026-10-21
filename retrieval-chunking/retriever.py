
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from pdf_reader import read_pdf
from chunker import create_chunks
from embedder import embed_chunks, get_embeddings


def retrieve_documents(question, embedded_chunks, top_k=5):
    """Retrieve the top-k chunks using cosine similarity."""

    if not embedded_chunks:
        raise ValueError("No embedded chunks available.")

    # Convert the question into an embedding
    question_embedding = get_embeddings(question)

    # Collect all chunk embeddings into a matrix
    chunk_embeddings = np.vstack([
        chunk["embedding"] for chunk in embedded_chunks
    ])

    # Calculate similarity between the question and every chunk
    scores = cosine_similarity(
        question_embedding.reshape(1, -1),
        chunk_embeddings
    )[0]

    # Get indices of the top-k highest scores
    top_indices = np.argsort(scores)[::-1][:top_k]

    # Return chunks with their similarity scores
    results = []

    for index in top_indices:
        result = {
            "chunk_id": embedded_chunks[index]["chunk_id"],
            "page": embedded_chunks[index]["page"],
            "text": embedded_chunks[index]["text"],
            "similarity": float(scores[index])
        }

        results.append(result)

    return results


if __name__ == "__main__":
    # Load PDF and generate embeddings
    pages = read_pdf("test.pdf")
    chunks = create_chunks(pages)

    print(f"Total chunks: {len(chunks)}")
    print("Generating embeddings...")

    embedded_chunks = embed_chunks(chunks)

    # Ask a question
    question = input("\nEnter your question: ")

    results = retrieve_documents(
        question,
        embedded_chunks,
        top_k=5
    )

    # Display retrieved documents
    print("\n========== RETRIEVED DOCUMENTS ==========")

    for rank, result in enumerate(results, start=1):
        print(f"\nRank: {rank}")
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"PDF Page: {result['page']}")
        print(f"Cosine Similarity: {result['similarity']:.4f}")
        print("-" * 50)
        print(result["text"])

    print("\n========== RETRIEVAL COMPLETE ==========")

