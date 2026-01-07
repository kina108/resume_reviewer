import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        pages = [p.extract_text() for p in pdf.pages]
    return "\n".join([p for p in pages if p])

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def process_file(uploaded_file):
    if uploaded_file is None:
        return None, "No file uploaded."

    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8"), None

    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file), None

    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file), None

    return None, "Unsupported file type. Use PDF, DOCX, or TXT."
