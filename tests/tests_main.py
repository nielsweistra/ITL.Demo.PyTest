# test_main.py
from fastapi.testclient import TestClient
from src.main import (  
    app,
)  

client = TestClient(app, base_url="http://localhost:8000")

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
