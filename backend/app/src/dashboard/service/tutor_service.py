from fastapi import HTTPException, status
from sqlmodel import Session, select
from fastapi_pagination.ext.sqlmodel import paginate

from ..models.models import Tutor, TutorCreate, TutorUpdate

def get_all_tutors_or_404(session: Session):
    tutors = paginate(session, select(Tutor))
    if not tutors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")
    return tutors

def get_tutor_by_id_or_404(session: Session, tutor_id: int):
    tutor = session.get(Tutor, tutor_id)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not found")
    return tutor

def create_tutor_or_404(session: Session, tutor: TutorCreate):
    tutor = Tutor.model_validate(tutor)
    session.add(tutor)
    session.commit()
    session.refresh(tutor)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not created")
    return tutor

def updaate_tutor_or_404(session: Session, tutor_id: int, tutor: TutorUpdate):
    db_tutor = session.get(Tutor, tutor_id)
    if not db_tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not found")
    tutor_data = tutor.model_dump(exclude_unset=True)
    for key, value in tutor_data.items():
        setattr(db_tutor, key, value)
    session.add(db_tutor)
    session.commit()
    session.refresh(db_tutor)
    return db_tutor

def delete_tutor_or_404(session: Session, tutor_id: int):
    tutor = session.get(Tutor, tutor_id)
    if not tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not found")
    session.delete(tutor)
    session.commit()
    return tutor

def get_tutor_by_name_or_404(session: Session, q: str):
    tutors = paginate(session, select(Tutor).where(   Tutor.first_name.contains(q) 
                                                    | Tutor.last_name1.contains(q)
                                                    | Tutor.last_name2.contains(q) 
                                                    | Tutor.email.contains(q) 
                                                    | Tutor.phone.contains(q) 
    ))
    
    if not tutors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")
    
    return tutors