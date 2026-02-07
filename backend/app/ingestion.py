import pdfplumber
from docx import Document
from fastapi import UploadFile

def extract_text(file: UploadFile) -> str:
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    if file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join(p.text for p in doc.paragraphs)

    raise ValueError("Unsupported file type")
