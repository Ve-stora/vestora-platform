from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Vestora Platform")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("app/templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

print("✅ Vestora Dashboard Running at http://127.0.0.1:8000")