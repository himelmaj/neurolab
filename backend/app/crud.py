from fastapi import APIRouter, Depends
from database import get_db, Session
from models import Student, Tutors, TypeRelationTutorStudent, RelStuTutTyp, Addressess

router = APIRouter()


@router.get("/")
def read_root():
    return {"students": "http://localhost:8000/students/", "tutors": "http://localhost:8000/tutors/", "types-relations-tutors-students": "http://localhost:8000/types-relations-tutors-students/", "rel-stu-tut-typ": "http://localhost:8000/rel-stu-tut-typ/"}


@router.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students


@router.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students


@router.get("/student/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id_student == student_id).first()
    return student


@router.get("/tutors/")
def read_tutors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tutors = db.query(Tutors).offset(skip).limit(limit).all()
    return tutors


@router.get("/tutor/{tutor_id}")
def read_tutors(tutor_id: int, db: Session = Depends(get_db)):
    tutors = db.query(Tutors).filter(Tutors.id_tutor == tutor_id).first()
    return tutors


@router.get("/types-relations-tutors-students/")
def read_typerelationtutorstudent(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    type_relation_tutor_student = db.query(
        TypeRelationTutorStudent).offset(skip).limit(limit).all()
    return type_relation_tutor_student


@router.get("/type-relation-tutor-student/{relation_type}")
def read_typerelationtutorstudent(relation_type: int, db: Session = Depends(get_db)):
    type_relation_tutor_student = db.query(TypeRelationTutorStudent).filter(
        TypeRelationTutorStudent.id_relation == relation_type).first()
    return type_relation_tutor_student


@router.get("/rel-stu-tut-typ/")
def read_relstututtyp(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rel_stu_tut_typ = db.query(RelStuTutTyp).offset(skip).limit(limit).all()
    result = []
    for rel in rel_stu_tut_typ:
        # result.append({
        #     "id_student": f'http://127.0.0.1:8000/student/{url.id_student}',
        #     "id_tutor": f'http://127.0.0.1:8000/tutor/{url.id_tutor}',
        #     "Relation": db.query(TypeRelationTutorStudent).filter( TypeRelationTutorStudent.id_relation == url.id_relation).first(),
        # })

        result.append({
            "Student": {"data": db.query(Student).filter(Student.id_student == rel.id_student).first(), "url": f'http://127.0.0.1:8000/student/{rel.id_student}'},
            "Tutor": {"data": db.query(Tutors).filter(Tutors.id_tutor == rel.id_tutor).first(), "url": f'http://127.0.0.1:8000/tutor/{rel.id_tutor}', },
            "Relation": db.query(TypeRelationTutorStudent).filter(TypeRelationTutorStudent.id_relation == rel.id_relation).first(),
        })
    return result

@router.get("/addressess/")
def read_addressess(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    addressess = db.query(Addressess).offset(skip).limit(limit).all()
    return addressess
