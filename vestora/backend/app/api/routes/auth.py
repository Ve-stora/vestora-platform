from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.db.database import get_db
from app.schemas.auth import UserRegister, UserLogin, Token, UserResponse
from app.services.auth_service import register_user, authenticate_user, create_access_token, verify_token
from app.core.config import settings
from app.models.user import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(email: str, full_name: str, password: str, db: Session = Depends(get_db)):
    user = register_user(db, email, full_name, password)
    if not user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email}, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "bearer", "user_id": user.id, "email": user.email}
