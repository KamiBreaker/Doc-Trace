import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def embed_clauses(clauses):
    if not OPENAI_API_KEY:
        # Fallback or error if no key is provided
        raise ValueError("OPENAI_API_KEY is not set")
    
    response = httpx.post(
        "https://api.openai.com/v1/embeddings",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "input": clauses,
            "model": "text-embedding-3-small"
        },
        timeout=60.0
    )
    data = response.json()
    return [item["embedding"] for item in data["data"]]