from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_read_student():
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["id_student"] == 1
    assert response.json()["id_user"] == None
    assert response.json()["first_name"] == "Alice"
    assert response.json()["last_name1"] == "Johnson"
    assert response.json()["last_name2"] == None
    assert response.json()["date_of_birth"] == "1995-09-30"
    assert response.json()["place_of_birth"] == "Village"
    assert response.json()["is_emancipated"] == True
    assert response.json()["email"] == "alice.j@example.com"
    assert response.json()["dni"] == "456789012"
    assert response.json()["id_address"] == None
    assert response.json()["created_by"] == None
    assert response.json()["updated_by"] == None
    assert response.json()["created_at"] == "2024-01-04T01:03:09"
    assert response.json()["updated_at"] == "2024-01-04T01:03:09"
    
def test_read_student_not_found():
    response = client.get("/students/21390128419872409821742190742")
    assert response.status_code == 404

def test_create_student():
    response = client.post("/students/",
        json= {
            "id_user": None,
            "first_name": "Bob",
            "last_name1": "Smith",
            "last_name2": None,
            "date_of_birth": "1995-09-30",
            "place_of_birth": "Village",
            "is_emancipated": False,
            "email": "bob.smith@example.com",
            "dni": "456789012",
            "id_address": None,
            "created_by": None,
            "updated_by": None,
            "created_at": "2024-01-04T01:03:09",
            "updated_at": "2024-01-04T01:03:09"
        }
    )
    assert response.status_code == 201