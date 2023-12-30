from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
# from app.models import Student, Tutors, RelStudentTutors, TypeRelationTutorStudent
from app.src.dashboard.schemas import StudentSchema, TutorSchema
from app.src.dashboard.models import Student, Tutor, TypeRelationTutorStudent
from typing import List, Optional

dashboard_router = APIRouter(
    prefix="/api/v1",
    tags=["Dashboard"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@dashboard_router.get("/students/tutors", response_model=List[StudentSchema])
def read_students_with_tutors(db: Session = Depends(get_db)):   
    db_students_tutors = db.query(Student).options(joinedload(Student.tutors)).all()
    if not db_students_tutors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students or Tutors not found")
    return db_students_tutors

@dashboard_router.get("/students/{student_id}/tutors", response_model=List[StudentSchema])
def read_students_tutors_by_student_id(student_id: int, db: Session = Depends(get_db)):
    db_student_tutors = db.query(Student).filter(Student.id_student == student_id).options(joinedload(Student.tutors)).all()
    if not db_student_tutors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return db_student_tutors

@dashboard_router.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_students = db.query(Student).offset(skip).limit(limit).all()
    if not db_students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Students not found")
    return db_students

# route to get student by id
@dashboard_router.get("/students/{student_id}")
def read_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id_student == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

# route to get student by name
@dashboard_router.get("/students")
def read_student_by_name(name: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.first_name == name).all()
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

# @dashboard_router.get("/students/{student_id}/tutors/")
# def read_student_tutors(student_id: int, db: Session = Depends(get_db)):
    
#     result = {}

#     student = db.query(Student).filter(Student.id_student == student_id).first()
    
#     if not student:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
#     result["student"] = student

#     relations = db.query(RelStudentTutors).filter(RelStudentTutors.id_student == student_id).all()
    
#     if not relations:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    
#     id_tutors = [rel.id_tutor for rel in relations]

#     tutors_list = db.query(Tutors).filter(Tutors.id_tutor.in_(id_tutors)).all()
    
#     if not tutors_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")

#     tutors_by_relation = {}
    
#     for tutor in tutors_list:
#         relation = db.query(TypeRelationTutorStudent).filter(TypeRelationTutorStudent.id_relation == tutor.id_relation).first()
        
#         if not relation:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relation Type not found")
        
#         relation_type = relation.relation_type
        
#         if relation_type not in tutors_by_relation:
            
#             tutors_by_relation[relation_type] = []
            
#         tutors_by_relation[relation_type].append(tutor)

#     result["tutors"] = tutors_by_relation

#     return result


# @dashboard_router.get("/tutors/")
# def read_tutors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tutors = db.query(Tutors).offset(skip).limit(limit).all()
#     if not tutors:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutors not found")
#     return tutors

# @dashboard_router.get("/tutors/{tutor_id}")
# def read_tutor(tutor_id: int, db: Session = Depends(get_db)):
#     tutor = db.query(Tutors).filter(Tutors.id_tutor == tutor_id).first()
#     if not tutor:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutor not found")
#     return tutor
