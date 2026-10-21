from pathlib import Path
from pypdf import PdfReader

def read_pdf(pdf_path):
    """extract text from a pdf, page by page"""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"pdf not found: {pdf_path}")
    reader = PdfReader(str(pdf_path))
    pages = []
    for page_number, page in enumerate(reader.pages, start = 1):
        text = page.extract_text() or ""
        pages.append({
            "page": page_number,
            "text": text.strip()
        })
    return pages

if __name__ == "__main__":
    pdf_path = "test.pdf"
    pages = read_pdf(pdf_path)
    print(f"total pages: {len(pages)}")
    for page in pages:
        print(f"\n--- page {page["page"]} ---")
        print(page["text"][:500])
    full_text = "\n".join(page["text"] for page in pages)
    print(f"\ntotal characters extracted: {len(full_text)}")

# Understand the code
# - PdfReader() opens the PDF file.
# - reader.pages lets us iterate through its pages.
# - page.extract_text() extracts the text from each page.
# - pages.append() stores the page number alongside its text.
# - text[:500] prints only the first 500 characters from each page, keeping the output manageable.