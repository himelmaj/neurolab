from fastapi import APIRouter, Depends, Query, status, Path
from sqlmodel import Session
from ..models.models import StudentRead, StudentCreate, StudentUpdate, StudentReadWithTutors
from app.database import init_db, get_session
from ..service import student_service as service
from app.utils import Page


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

@router.get("/{student_id}/tutors", response_model=StudentReadWithTutors, status_code=status.HTTP_200_OK)
def read_student_tutors(*, session: Session = Depends(get_session), student_id: int = Path(..., title="Student ID", description="ID of the student to read")):
    db_student = service.get_student_by_id_or_404(session, student_id)
    return db_student
