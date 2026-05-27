# Vestora Platform

**AI-Powered Retail Investor Intelligence for Uganda**

Vestora is a modern platform designed to empower everyday Ugandan investors with real-time market insights from the Uganda Securities Exchange (USE), intelligent portfolio tracking, and financial education — all powered by AI.

---

## 🎯 Vision
To make professional-grade investment tools accessible to every Ugandan — from first-time investors in Kampala to those in upcountry towns.

---

## ✨ Key Features (MVP)

- ✅ **User Authentication** (Register & Login)
- ✅ **Market Dashboard** — Live mock data from Uganda Securities Exchange (USE)
- ✅ **AI Investment Assistant** — Ask questions in plain English about Ugandan stocks
- ✅ **Portfolio Tracking** — Create and monitor your investment portfolio
- 🔄 Financial education content (coming soon)

---

## 🛠 Tech Stack

- **Backend**: FastAPI + Python + SQLAlchemy + JWT
- **Frontend**: React + TypeScript + Vite + Tailwind CSS
- **Database**: PostgreSQL (SQLite for local dev)
- **AI**: Groq / OpenAI compatible
- **Containerization**: Docker + Docker Compose

---

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Ve-stora/vestora-platform.git
cd vestora-platform

2. Run with Docker (Recommended)
docker-compose up --build
3. Access the Application
Frontend: http://localhost:5173
Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs
Alternative: Local Development
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (new terminal)

cd frontend
npm install
npm run dev

📁 Project Structure
vestora-platform/
├── backend/              # FastAPI backend
├── frontend/             # React frontend
├── docs/                 # Documentation
├── docker-compose.yml
└── README.md
API Endpoints (Key ones)
POST /api/auth/register — Create account
POST /api/auth/login — User login
GET /api/market/stocks — Ugandan market data
POST /api/ai/assistant — AI investment assistant
GET /api/portfolio — View portfolio


Access the app:
Frontend: http://localhost:5173
Backend API: http://localhost:8000
API Documentation: http://localhost:8000/docs
Health Check: http://localhost:8000/health


Screenshots
(Add 3-4 screenshots here after you have a working demo)
Login Screen
Market Dashboard
AI Assistant Chat
Portfolio Page
Why This Matters for Uganda
Democratizes access to capital markets
Supports financial inclusion
Promotes local innovation in fintech
Aligns with Uganda’s digital transformation goals
Submission for Government Systems Prototype Showcase
Team: Ve-stora
Focus Area: Revenue & Financial Management + Citizen Engagement & Service Delivery
Prototype Status: Functional MVP with core flows working
Contact
Email: [your-email]
Phone: [optional]
Made with ❤️ for Ugandan Investors
---
