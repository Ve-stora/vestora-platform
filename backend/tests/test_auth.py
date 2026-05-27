from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    res = client.post("/api/auth/register", json={
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    })
    assert res.status_code == 201

def test_login_invalid():
    res = client.post("/api/auth/login",
        data={"username": "wrong@example.com", "password": "wrong"})
    assert res.status_code == 401
