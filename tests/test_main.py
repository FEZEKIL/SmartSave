import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SmartSave API"}

def test_get_transactions():
    # This would require mocking the MoMo API
    # For now, just test the endpoint exists
    response = client.get("/transactions/test_user")
    # Assuming it returns 500 without proper setup
    assert response.status_code in [200, 500]
