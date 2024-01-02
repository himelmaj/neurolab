from fastapi.testclient import TestClient
from backend.app.src.students.router import router as students_router

client = TestClient(students_router)

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert response.json() == []