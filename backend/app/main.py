from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, market, portfolio, education, alerts, ai_assistant
from app.core.config import settings
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vestora API", version="1.0.0", description="AI-powered retail investor platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(market.router, prefix="/api/market", tags=["Market"])
app.include_router(portfolio.router, prefix="/api/portfolio", tags=["Portfolio"])
app.include_router(education.router, prefix="/api/education", tags=["Education"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(ai_assistant.router, prefix="/api/ai", tags=["AI Assistant"])

@app.get("/")
def root():
    return {"message": "Vestora API is running", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}