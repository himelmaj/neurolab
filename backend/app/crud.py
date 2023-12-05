from fastapi import APIRouter, Body
from database import get_students

router = APIRouter()

@router.get("/students/")
def read_students(skip: int = 0, limit: int = 10):
    students = get_students(skip, limit)
    return students