from app.src.students.models import Student
from sqlalchemy.orm import Session

def get_students(db: Session, skip: int, limit: int):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id_student == student_id).first()

def get_student_by_name(db: Session, student_name: str):
    return db.query(Student).filter(Student.first_name == student_name).all()