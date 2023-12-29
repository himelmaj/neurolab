from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student, Tutors, RelStudentTutors, TypeRelationTutorStudent

dashboard_router = APIRouter(
    prefix="/api/v1",
    tags=["Dashboard"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)

@dashboard_router.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students not found")
    return students

@dashboard_router.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id_student == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

# @dashboard_router.get("/students/{student_id}/tutors/")
# def read_student_tutors(student_id: int, db: Session = Depends(get_db)):
    
#     relations = db.query(RelStudentTutors).filter(RelStudentTutors.id_student == student_id).all()
    
#     if not relations:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
#     id_tutors = [rel.id_tutor for rel in relations]
#     tutors = db.query(Tutors).filter(Tutors.id_tutor.in_(id_tutors)).all()
    
#     if not tutors:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")
#     return tutors

@dashboard_router.get("/students/{student_id}/tutors/")
def read_student_tutors(student_id: int, db: Session = Depends(get_db)):
    
    result = {}

    student = db.query(Student).filter(Student.id_student == student_id).first()
    
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    result["student"] = student

    relations = db.query(RelStudentTutors).filter(RelStudentTutors.id_student == student_id).all()
    
    if not relations:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    
    id_tutors = [rel.id_tutor for rel in relations]

    tutors_list = db.query(Tutors).filter(Tutors.id_tutor.in_(id_tutors)).all()
    
    if not tutors_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")

    tutors_by_relation = {}
    
    for tutor in tutors_list:
        relation = db.query(TypeRelationTutorStudent).filter(TypeRelationTutorStudent.id_relation == tutor.id_relation).first()
        
        if not relation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relation Type not found")
        
        relation_type = relation.relation_type
        
        if relation_type not in tutors_by_relation:
            
            tutors_by_relation[relation_type] = []
            
        tutors_by_relation[relation_type].append(tutor)

    result["tutors"] = tutors_by_relation

    return result


@dashboard_router.get("/tutors/")
def read_tutors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tutors = db.query(Tutors).offset(skip).limit(limit).all()
    if not tutors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")
    return tutors

@dashboard_router.get("/tutors/{tutor_id}")
def read_tutor(tutor_id: int, db: Session = Depends(get_db)):
    tutor = db.query(Tutors).filter(Tutors.id_tutor == tutor_id).first()
    if not tutor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not found")
    return tutor
