
from pdf_reader import read_pdf

pages = read_pdf("test.pdf")

print("Number of pages:", len(pages))

total_chars = sum(len(page.get("text", "")) for page in pages)
print("Total characters:", total_chars)

for page in pages[:3]:
    print(
        "Page:", page.get("page"),
        "| Characters:", len(page.get("text", "")),
        "| Preview:", repr(page.get("text", "")[:100])
    )
