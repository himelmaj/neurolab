from fastapi import APIRouter, Depends, Query, status, Path
from sqlmodel import Session
from ..models import models
from ..service import course_service as service
from app.database import get_session
from app.utils import Page
from typing import List


router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/", response_model=Page[models.CourseRead], status_code=status.HTTP_200_OK)
def read_courses(*, session: Session = Depends(get_session)):
    db_courses = service.get_all_courses_or_404(session)
    return db_courses

@router.get("/{course_id}", response_model=models.CourseRead, status_code=status.HTTP_200_OK)
def read_course(*, session: Session = Depends(get_session), course_id: int = Path(..., title="Course ID", description="ID of the course to read")):
    db_course = service.get_course_by_id_or_404(session, course_id)
    return db_course

@router.get("/search/", response_model=Page[models.CourseRead], status_code=status.HTTP_200_OK)
def search_courses(*, session: Session = Depends(get_session), course_name: str = Query(..., title="Search query", description="Query to search courses")):
    db_courses = service.get_course_by_name_or_404(session, course_name)
    return db_courses

@router.post("/", response_model=models.CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(*, course: models.CourseCreate, session: Session = Depends(get_session)):
    db_course = service.create_course_or_404(session, course)
    return db_course

@router.patch("/{course_id}", response_model=models.CourseRead, status_code=status.HTTP_200_OK)
def update_course(*, session: Session = Depends(get_session), course_id: int = Path(..., title="Course ID", description="ID of the course to update"), course: models.CourseUpdate):
    db_course = service.update_course_or_404(session, course_id, course)
    return db_course

@router.delete("/{course_id}", response_model=models.CourseRead, status_code=status.HTTP_200_OK)
def delete_course(*, session: Session = Depends(get_session), course_id: int = Path(..., title="Course ID", description="ID of the course to delete")):
    db_course = service.delete_course_or_404(session, course_id)
    return db_course

@router.get("/{course_id}/students/", response_model=List[models.StudentRead], status_code=status.HTTP_200_OK)
def read_students_of_course(*, session: Session = Depends(get_session), course_id: int = Path(..., title="Course ID", description="ID of the course to read")):
    db_course = service.get_course_by_id_or_404(session, course_id)
    return db_course.students

