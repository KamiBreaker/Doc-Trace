from app.db import SessionLocal, engine
from app.models import Base, Document
import uuid

def test_connection():
    try:
        # Try to connect
        connection = engine.connect()
        print("Successfully connected to the database.")
        connection.close()
        
        # Try to query
        db = SessionLocal()
        count = db.query(Document).count()
        print(f"Successfully queried documents table. Count: {count}")
        
        # Try to insert
        new_doc = Document(title="Test Document")
        db.add(new_doc)
        db.commit()
        print("Successfully inserted a test document.")
        
        db.delete(new_doc)
        db.commit()
        print("Successfully cleaned up test document.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()
