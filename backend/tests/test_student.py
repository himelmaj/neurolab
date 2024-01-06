from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert len(response.json()) == 2