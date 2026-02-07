from fastapi import FastAPI, UploadFile, File, Depends, Form
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Document, DocumentVersion, Clause, Embedding
from app.ingestion import extract_text
from app.chunking import chunk_into_clauses
from app.embeddings import embed_clauses
from app.diff_engine import semantic_diff
from app.qa_engine import answer_question
from app.schemas import DiffResponse
import uuid

app = FastAPI(title="DocuTrace AI")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health():
    return {"status": "ok"}

def save_document(db: Session, title: str, text: str, chunks: list[str], vecs: list):
    doc = Document(title=title)
    db.add(doc)
    db.flush()

    version = DocumentVersion(
        document_id=doc.id,
        version_number=1,
        raw_text=text
    )
    db.add(version)
    db.flush()

    for i, (chunk_text, vec) in enumerate(zip(chunks, vecs)):
        clause = Clause(
            version_id=version.id,
            clause_index=i,
            text=chunk_text
        )
        db.add(clause)
        db.flush()

        embedding = Embedding(
            clause_id=clause.id,
            vector=vec.tolist()
        )
        db.add(embedding)
    
    db.commit()
    return doc

@app.post("/compare", response_model=DiffResponse)
async def compare(
    old_doc: UploadFile = File(...),
    new_doc: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    old_text = extract_text(old_doc)
    new_text = extract_text(new_doc)

    old_chunks = chunk_into_clauses(old_text)
    new_chunks = chunk_into_clauses(new_text)

    old_vecs = embed_clauses(old_chunks)
    new_vecs = embed_clauses(new_chunks)

    # Save documents to DB
    save_document(db, old_doc.filename, old_text, old_chunks, old_vecs)
    save_document(db, new_doc.filename, new_text, new_chunks, new_vecs)

    diffs = semantic_diff(old_chunks, new_chunks, old_vecs, new_vecs)
    return {"diffs": diffs}

@app.post("/qa")
def qa(question: str, clauses: list[str]):
    return answer_question(question, clauses)