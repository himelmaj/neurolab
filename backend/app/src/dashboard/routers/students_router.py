from fastapi import APIRouter, Depends, Query, status, Path
from sqlmodel import Session
from ..models.models import StudentRead, StudentCreate, StudentUpdate, StudentReadWithTutors, Student
from ..models import models
from app.database import get_session
from ..service import student_service as service
from app.utils import Page
from typing import List

router = APIRouter(
    prefix="/students",
    tags=["Students"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
    
    
@router.get("/", response_model=Page[StudentRead], status_code=status.HTTP_200_OK)
def read_students(*, session: Session = Depends(get_session)):
    db_students = service.get_all_students_or_404(session)
    return db_students

@router.get("/{student_id}", response_model=StudentRead, status_code=status.HTTP_200_OK)
def read_student(*, session: Session = Depends(get_session),  student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
    db_student = service.get_student_by_id_or_404(session, student_id)
    return db_student

@router.get("/search/", response_model=Page[StudentRead], status_code=status.HTTP_200_OK)
def search_students(*, session: Session = Depends(get_session), q: str = Query(..., title="Search query", description="Query to search students")):
    db_students = service.get_student_by_name_or_404(session, q)
    return db_students

@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(*, student: StudentCreate, session: Session = Depends(get_session)):
    db_student = service.create_student_or_404(session, student)
    return db_student

@router.patch("/{student_id}", response_model=StudentRead, status_code=status.HTTP_200_OK)
def update_student(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to update"), student: StudentUpdate):
    db_student = service.update_student_or_404(session, student_id, student)
    return db_student

@router.delete("/{student_id}", response_model=StudentRead, status_code=status.HTTP_200_OK)
def delete_student(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to delete")):
    db_student = service.delete_student_or_404(session, student_id)
    return db_student

# @router.get("/{student_id}/tutors/", response_model=StudentReadWithTutors, status_code=status.HTTP_200_OK)
# def read_student_tutors(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
#     db_student = service.get_student_by_id_or_404(session, student_id)
#     return db_student

@router.get("/{student_id}/tutors/", response_model=List[models.TutorRead], status_code=status.HTTP_200_OK)
def read_tutors_of_student(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
    db_student = service.get_student_by_id_or_404(session, student_id)
    return db_student.tutors

@router.get("/{student_id}/course/", response_model=models.CourseRead, status_code=status.HTTP_200_OK)
def read_course_of_student(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
    db_student = service.get_student_by_id_or_404(session, student_id)
    return db_student.course

# @router.get("/{student_id}/course/", response_model=models.StudentReadWithCourse, status_code=status.HTTP_200_OK)
# def read_student_course(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
#     db_student = service.get_student_by_id_or_404(session, student_id)
#     return db_student