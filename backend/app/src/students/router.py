from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional, Annotated
from app.database import get_db
from app.utils import common_parameters
from app.src.students.models import Student
from app.src.students import service
router = APIRouter(
    prefix="/students",
    tags=["Students"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/")
def read_students(commons: Annotated[dict, Depends(common_parameters)], db: Session = Depends(get_db)):
    db_students = service.get_students(db, commons["skip"], commons["limit"])
    if not db_students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students not found")
    return db_students

@router.get("/{student_id}")
def read_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = service.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

# @router.get("/")
# def read_student_by_name(name: str | None = None, db: Session = Depends(get_db)):
#     student = service.get_student_by_name(db, name)
#     if not student:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
#     return student