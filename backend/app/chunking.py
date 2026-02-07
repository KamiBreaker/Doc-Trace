import re

def chunk_into_clauses(text: str, max_len: int = 400):
    sentences = re.split(r"(?<=[.;])\s+", text)
    chunks, current = [], ""

    for s in sentences:
        if len(current) + len(s) <= max_len:
            current += " " + s
        else:
            chunks.append(current.strip())
            current = s

    if current.strip():
        chunks.append(current.strip())

    return chunks
