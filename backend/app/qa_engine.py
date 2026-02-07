from transformers import pipeline

# Using a much smaller model for constrained environments (Render Free Tier)
qa = pipeline(
    "question-answering",
    model="mrm8488/tinyroberta-squad2"
)

def answer_question(question: str, clauses: list[str]):
    context = " ".join(clauses[:6])
    result = qa(question=question, context=context)
    return {
        "answer": result["answer"],
        "confidence": float(result["score"])
    }
