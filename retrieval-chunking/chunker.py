
from pdf_reader import read_pdf

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


def create_chunks(pages, chunk_size=CHUNK_SIZE,
                  overlap=CHUNK_OVERLAP):

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid overlap")

    chunks = []
    step_size = chunk_size - overlap

    print(f"Pages received: {len(pages)}")

    for page in pages:
        text = page.get("text", "")
        page_number = page.get("page", "?")

        print(
            f"Page {page_number}: "
            f"{len(text)} characters"
        )

        for start in range(0, len(text), step_size):
            chunk_text = text[start:start + chunk_size]

            if chunk_text.strip():
                chunks.append({
                    "chunk_id": len(chunks),
                    "page": page_number,
                    "text": chunk_text
                })

    return chunks


if __name__ == "__main__":
    pages = read_pdf("test.pdf")

    print(f"Total pages read: {len(pages)}")

    chunks = create_chunks(pages)

    print(f"\nTotal chunks created: {len(chunks)}")

    for chunk in chunks[:3]:
        print(f"\nChunk ID: {chunk['chunk_id']}")
        print(f"Page: {chunk['page']}")
        print(f"Text: {chunk['text'][:150]}")

    print("\nChunking complete.")
