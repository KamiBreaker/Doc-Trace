from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, ARRAY, DOUBLE_PRECISION
from app.db import Base
import uuid

class Document(Base):
    __tablename__ = "documents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text)

class DocumentVersion(Base):
    __tablename__ = "document_versions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"))
    version_number = Column(Integer)
    raw_text = Column(Text)
    created_at = Column(TIMESTAMP)

class Clause(Base):
    __tablename__ = "clauses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version_id = Column(UUID(as_uuid=True), ForeignKey("document_versions.id"))
    clause_index = Column(Integer)
    text = Column(Text)

class Embedding(Base):
    __tablename__ = "embeddings"
    clause_id = Column(UUID(as_uuid=True), ForeignKey("clauses.id"), primary_key=True)
    vector = Column(ARRAY(DOUBLE_PRECISION))
