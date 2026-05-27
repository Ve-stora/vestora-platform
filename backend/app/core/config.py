from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vestora Platform"
    API_V1_STR: str = "/api"
    DATABASE_URL: str = "sqlite:///./vestora.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
