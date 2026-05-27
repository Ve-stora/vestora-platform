from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vestora API"
    DATABASE_URL: str = "postgresql://user:password@db:5432/vestora"
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOWED_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    OPENAI_API_KEY: str = "sk-your-key"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
