from fastapi import APIRouter, Depends
from database import get_db, Session
from models import Student

router = APIRouter()

@router.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
