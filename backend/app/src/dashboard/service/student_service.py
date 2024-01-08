from fastapi import HTTPException, status
from sqlmodel import Session, select
from fastapi_pagination.ext.sqlmodel import paginate
from ..models.models import Student, StudentCreate, StudentUpdate

def get_all_students_or_404(session: Session):
    students = paginate(session, select(Student))
    
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students not found")
    
    return students

def get_student_by_id_or_404(session: Session, student_id: int):
    student = session.get(Student, student_id)
    
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    return student

def create_student_or_404(session: Session, student: StudentCreate):
    student = Student.model_validate(student)
    session.add(student)
    session.commit()
    session.refresh(student)
    
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not created")
    
    return student

def update_student_or_404(session: Session, student_id: int, student: StudentUpdate):
    db_student = session.get(Student, student_id)
    
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    student_data = student.model_dump(exclude_unset=True)
    
    for key, value in student_data.items():
        setattr(db_student, key, value)
        
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

def delete_student_or_404(session: Session, student_id: int):
    student = session.get(Student, student_id)
    
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    session.delete(student)
    session.commit()
    return student

def get_student_by_name_or_404(session: Session, q: str):
    students = paginate(session, select(Student).where(  Student.first_name.contains(q) 
                                                       | Student.last_name1.contains(q) 
                                                       | Student.last_name2.contains(q)))
    
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    return students