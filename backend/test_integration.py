from app.db import SessionLocal
from app.models import Document, DocumentVersion, Clause, Embedding
import uuid

def test_full_insert():
    db = SessionLocal()
    try:
        doc = Document(title="Test DB Integration")
        db.add(doc)
        db.flush()
        
        version = DocumentVersion(
            document_id=doc.id,
            version_number=1,
            raw_text="Test raw text"
        )
        db.add(version)
        db.flush()
        
        clause = Clause(
            version_id=version.id,
            clause_index=0,
            text="Test clause"
        )
        db.add(clause)
        db.flush()
        
        emb = Embedding(
            clause_id=clause.id,
            vector=[0.1, 0.2, 0.3]
        )
        db.add(emb)
        db.commit()
        print("Successfully performed full integration insert.")
        
        # Cleanup
        db.delete(doc) # Cascade should handle others
        db.commit()
        print("Successfully cleaned up.")
    except Exception as e:
        db.rollback()
        print(f"Failed integration test: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_full_insert()
