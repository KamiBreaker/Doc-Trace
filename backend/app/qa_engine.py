import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def answer_question(question: str, clauses: list[str]):
    if not OPENAI_API_KEY:
        return {"answer": "OpenAI API Key not configured.", "confidence": 0}

    context = "\n".join(clauses[:10])
    
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Answer the question based strictly on the provided context."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
            ]
        },
        timeout=60.0
    )
    
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    
    return {
        "answer": answer,
        "confidence": 1.0
    }