from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

def test_greet():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"messages":"Hello World"}


