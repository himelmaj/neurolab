from fastapi import APIRouter, Depends, Query, status, Path
from sqlmodel import Session
from app.database import get_session
from ..models.models import TutorRead, TutorCreate, TutorReadWithStudents
from ..models import models
from ..service import tutor_service as service
from app.utils import Page
from typing import List
router = APIRouter(
    prefix="/tutors",
    tags=["Tutors"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@router.get("/", response_model=Page[TutorRead], status_code=status.HTTP_200_OK)
def read_tutors(*, session: Session = Depends(get_session)):
    db_tutors = service.get_all_tutors_or_404(session)
    return db_tutors

@router.get("/{tutor_id}", response_model=TutorRead, status_code=status.HTTP_200_OK)
def read_tutor(*, session: Session = Depends(get_session), tutor_id: int = Path(..., title="Tutor ID", description="ID of the tutor to read")):
    db_tutor = service.get_tutor_by_id_or_404(session, tutor_id)
    return db_tutor

@router.get("/search/", response_model=Page[TutorRead], status_code=status.HTTP_200_OK)
def search_tutors(*, session: Session = Depends(get_session), q: str = Query(..., title="Search query", description="Query to search tutors")):
    db_tutors = service.get_tutor_by_name_or_404(session, q)
    return db_tutors

@router.post("/", response_model=TutorRead, status_code=status.HTTP_201_CREATED)
def create_tutor(*, tutor: TutorCreate, session: Session = Depends(get_session)):
    db_tutor = service.create_tutor_or_404(session, tutor)
    return db_tutor

@router.patch("/{tutor_id}", response_model=TutorRead, status_code=status.HTTP_200_OK)
def update_tutor(*, session: Session = Depends(get_session), tutor_id: int = Path(..., title="Tutor ID", description="ID of the tutor to update"), tutor: TutorCreate):
    db_tutor = service.update_tutor(session, tutor_id, tutor)
    return db_tutor

@router.delete("/{tutor_id}", response_model=TutorRead, status_code=status.HTTP_200_OK)
def delete_tutor(*, session: Session = Depends(get_session), tutor_id: int = Path(..., title="Tutor ID", description="ID of the tutor to delete")):
    db_tutor = service.delete_tutor_or_404(session, tutor_id)
    return db_tutor

# @router.get("/{tutor_id}/students", response_model=TutorReadWithStudents, status_code=status.HTTP_200_OK)
# def read_tutor_students(*, session: Session = Depends(get_session), tutor_id: int = Path(..., title="Tutor ID", description="ID of the tutor to read")):
#     db_tutor = service.get_tutor_by_id_or_404(session, tutor_id)
#     return db_tutor

@router.get("/{tutor_id}/students", response_model=List[models.StudentRead], status_code=status.HTTP_200_OK)
def read_tutor_students(*, session: Session = Depends(get_session), tutor_id: int = Path(..., title="Tutor ID", description="ID of the tutor to read")):
    db_tutor = service.get_tutor_by_id_or_404(session, tutor_id)
    return db_tutor.students