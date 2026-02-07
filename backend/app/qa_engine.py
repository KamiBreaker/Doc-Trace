from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2"
)

def answer_question(question: str, clauses: list[str]):
    context = " ".join(clauses[:6])
    result = qa(question=question, context=context)
    return {
        "answer": result["answer"],
        "confidence": float(result["score"])
    }
