from fastapi.testclient import TestClient
from fastapi import status
from app.src.students.router import router as students_router

client = TestClient(students_router)

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []