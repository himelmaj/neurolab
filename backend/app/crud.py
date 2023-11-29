from sqlalchemy.orm import Session
from . import models, schemas

def add_student(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.add(models.Student).offset(skip).limit(limit).all()
    return students
