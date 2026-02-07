CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE document_versions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
    version_number INT NOT NULL,
    raw_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE (document_id, version_number)
);

CREATE TABLE clauses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    version_id UUID REFERENCES document_versions(id) ON DELETE CASCADE,
    clause_index INT,
    text TEXT
);

CREATE TABLE embeddings (
    clause_id UUID REFERENCES clauses(id) ON DELETE CASCADE,
    vector FLOAT8[]
);
