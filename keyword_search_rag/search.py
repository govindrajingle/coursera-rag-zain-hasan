from extract_text import extract_text, parse_records
from preprocessing import preprocess
from inverted_index import build_inverted_index


def build_document_lookup(records):

    return {record["doc_id"]: record for record in records}


def search(query, index, document_lookup):

    tokens = preprocess(query)

    result_ids = set()

    for token in tokens:

        if token in index:
            result_ids.update(index[token])

    results = []

    for doc_id in sorted(result_ids):
        results.append(document_lookup[doc_id])

    return results


if __name__ == "__main__":

    text = extract_text("indian-states-and-districts.pdf")

    records = parse_records(text)

    index = build_inverted_index(records)

    document_lookup = build_document_lookup(records)

    results = search("hyderabad", index, document_lookup)

    for record in results:
        print(record)
