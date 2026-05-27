# USE Insight — Intelligent Retail Investor Platform for Uganda

## Quick Start

### Option 1: Docker (recommended)
```bash
docker-compose up --build
```
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Option 2: Local Development

**Backend**
```bash
cd backend
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables
Copy `backend/.env` and fill in:
- `SECRET_KEY` — random secure string
- `OPENAI_API_KEY` — from platform.openai.com
- `DATABASE_URL` — update if not using Docker

## Project Structure
```
use-insight/
├── backend/          FastAPI + PostgreSQL
│   └── app/
│       ├── api/      Route handlers
│       ├── ai/       AI assistant
│       ├── models/   Database models
│       ├── schemas/  Pydantic schemas
│       └── services/ Business logic
├── frontend/         React + Tailwind
│   └── src/
│       ├── api/      API clients
│       ├── components/
│       ├── pages/
│       └── store/    Zustand state
└── docker-compose.yml
```
