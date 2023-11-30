from fastapi import APIRouter, Body
from database import get_students

router = APIRouter()

@router.get("/students/")
async def read_students(skip: int = 0, limit: int = 10):
    students = await get_students(skip, limit)
    return students