from extract_text import extract_text, parse_records
from preprocessing import preprocess

text = extract_text("indian-states-and-districts.pdf")

records = parse_records(text)

first_record = records[0]

print(first_record)

print("\nDistrict Tokens:")
print(preprocess(first_record["district"]))

print("\nState Tokens:")
print(preprocess(first_record["state"]))
