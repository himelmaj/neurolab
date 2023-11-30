from fastapi import FastAPI
from crud import router
app = FastAPI()

app.include_router(router)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
        
# @app.get("/students/")
# def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     students = db.query(models.Student).offset(skip).limit(limit).all()
#     return students

# @app.get("/student/{student_id}")
# def read_student(student_id: int, db: Session = Depends(get_db)):
#     student = db.query(models.Student).filter(models.Student.id_student == student_id).first()
#     return student


# @app.get("/tutors/")
# def read_tutors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tutors = db.query(models.Tutors).offset(skip).limit(limit).all()
#     return tutors

# @app.get("/tutor/{tutor_id}")
# def read_tutors(tutor_id: int, db: Session = Depends(get_db)):
#     tutors = db.query(models.Tutors).filter(models.Tutors.id_tutor == tutor_id).first()
#     return tutors

# @app.get("/typerelationtutorstudent/")
# def read_typerelationtutorstudent(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     type_relation_tutor_student = db.query(models.TypeRelationTutorStudent).offset(skip).limit(limit).all()
#     return type_relation_tutor_student

# @app.get("/typerelationtutorstudent/{relation_type}")
# def read_typerelationtutorstudent(relation_type: int, db: Session = Depends(get_db)):
#     type_relation_tutor_student = db.query(models.TypeRelationTutorStudent).filter(models.TypeRelationTutorStudent.id_relation == relation_type).first()
#     return type_relation_tutor_student

# @app.get("/relstututtyp/")
# def read_relstututtyp(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     rel_stu_tut_typ = db.query(models.RelStuTutTyp).offset(skip).limit(limit).all()
#     result = []
#     for url in rel_stu_tut_typ:
#         result.append({
#             "id_student": f'http://127.0.0.1:8000/student/{url.id_student}',
#             "id_tutor": f'http://127.0.0.1:8000/tutor/{url.id_tutor}',
#             "id_relation": f'http://127.0.0.1:8000/typerelationtutorstudent/{url.id_relation}',
#         })
#     return result

# @app.get("/database")
# async def read_root():
#    return ping_database()