from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai.assistant import ask_assistant

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    context: str = ""

@router.post("/ask")
async def ask(payload: QuestionRequest):
    try:
        answer = await ask_assistant(payload.question, payload.context)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
