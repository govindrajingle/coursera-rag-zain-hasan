from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load documents
with open("documents.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Create TF-IDF matrix
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query = input("Ask: ")

query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix)

results = list(enumerate(scores[0]))

results.sort(key=lambda x: x[1], reverse=True)

print("\nTop Results:\n")

for idx, score in results[:3]:
    print(f"Score={score:.4f}")
    print(documents[idx])
    print()
