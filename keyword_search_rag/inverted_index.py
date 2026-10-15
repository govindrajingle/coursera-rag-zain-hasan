from collections import defaultdict

from extract_text import extract_text, parse_records
from preprocessing import preprocess


def build_inverted_index(records):

    inverted_index = defaultdict(set)

    for record in records:

        doc_id = record["doc_id"]

        district_tokens = preprocess(record["district"])

        state_tokens = preprocess(record["state"])

        all_tokens = district_tokens + state_tokens

        for token in all_tokens:
            inverted_index[token].add(doc_id)

    return inverted_index


if __name__ == "__main__":

    text = extract_text("indian-states-and-districts.pdf")

    records = parse_records(text)

    index = build_inverted_index(records)

    print("adilabad ->", index["adilabad"])

    print("hyderabad ->", index["hyderabad"])

    print("andhra ->", sorted(index["andhra"])[:10])
