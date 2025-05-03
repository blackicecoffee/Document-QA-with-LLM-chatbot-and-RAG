from pypdf import PdfReader

def extract_text(file):
    all_texts = {}

    reader = PdfReader(file)

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            all_texts[f"page_{page_num}"] = text
        else:
            all_texts[f"page_{page_num}"] = ""
    
    return all_texts