try:
    from pydantic_settings import BaseSettings
except Exception:
    try:
        from pydantic import BaseSettings
    except Exception:
        raise ImportError(
            "Neither 'pydantic_settings' nor 'pydantic' is available; install 'pydantic' or 'pydantic-settings'."
        )

from typing import List

class Settings(BaseSettings):
    # Project Config
    PROJECT_NAME: str = "Vestora Platform"
    API_V1_STR: str = "/api"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/use_insight"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API Keys
    OPENAI_API_KEY: str = ""
    ALPHA_VANTAGE_API_KEY: str = ""
    
    # USE Market Data
    USE_DATA_PROVIDER: str = "mock"  # Options: mock, alpha_vantage, yfinance, direct_api
    USE_API_BASE_URL: str = "https://www.use.or.ug/api"
    USE_DATA_UPDATE_INTERVAL: int = 300  # seconds (5 minutes)
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000", "http://localhost:8000"]
    
    # Cache Settings
    CACHE_TTL: int = 300  # 5 minutes
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
