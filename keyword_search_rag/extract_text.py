import fitz


def extract_text(pdf_path):
    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:
        text += page.get_text()

    return text


def parse_records(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    records = []

    i = 0

    while i < len(lines):

        if lines[i].isdigit():

            try:
                record = {
                    "doc_id": int(lines[i]),
                    "district": lines[i + 1],
                    "state": lines[i + 2],
                }

                records.append(record)

                i += 3

            except IndexError:
                break

        else:
            i += 1

    return records


if __name__ == "__main__":

    text = extract_text("indian-states-and-districts.pdf")

    records = parse_records(text)

    print("Total Records:", len(records))

    print("\nFirst 5 Records:\n")

    for record in records[:5]:
        print(record)
