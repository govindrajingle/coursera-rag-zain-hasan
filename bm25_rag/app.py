import ollama
from rank_bm25 import BM25Okapi

docs = [
    "Apple makes iPhone and MacBook products.",
    "Python is widely used for machine learning.",
    "BM25 is a powerful keyword search algorithm.",
    "RAG combines retrieval and generation.",
    "Qwen is an open source language model.",
]

tokenized_docs = [d.lower().split() for d in docs]

bm25 = BM25Okapi(tokenized_docs)

question = input("Question: ")

scores = bm25.get_scores(question.lower().split())

ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

context = "\n".join([doc for doc, score in ranked[:2]])

prompt = f"""
Answer using only the context.

Context:
{context}

Question:
{question}
"""

response = ollama.chat(
    model="qwen2.5:3b", messages=[{"role": "user", "content": prompt}]
)

print(response["message"]["content"])
