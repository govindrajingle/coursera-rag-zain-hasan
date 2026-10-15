import pymupdf

pdf_path = "indian-states-and-districts.pdf"
documents = []
doc = pymupdf.open(pdf_path)
for page_num, page in enumerate(doc):
    documents.append({"doc_id": page_num, "text": page.get_text()})
print(documents[:2])
