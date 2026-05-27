from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from openai import OpenAI
from app.core.config import settings
from app.db.database import get_db

router = APIRouter()

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_current_user_id(db: Session = Depends(get_db)) -> int:
    return 1

@router.post("/chat")
def chat_with_assistant(message: dict, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    user_message = message.get("message", "")
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are Vestora, an AI financial assistant helping retail investors in Uganda's capital markets. Provide clear, simple investment advice."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content
        return {
            "user_message": user_message,
            "assistant_message": assistant_message
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with AI: {str(e)}")

@router.post("/ask")
def ask_question(question: dict, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return chat_with_assistant(question, user_id, db)