from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR, DATE, DATETIME, LONGTEXT, BOOLEAN
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = "students"
    id_student = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    idalu = Column(INTEGER(10), nullable=False)
    first_name = Column(VARCHAR(30), nullable=False, index=True)
    last_name = Column(VARCHAR(30), nullable=False)
    date_of_birth = Column(DATE, nullable=False)
    is_emancipated = Column(BOOLEAN, nullable=False)
    email = Column(VARCHAR(30), nullable=False)
    nif = Column(VARCHAR(9), nullable=True)
    cip = Column(VARCHAR(15), nullable=False)
    
class Tutors(Base):
    __tablename__ = "tutors"
    id_tutor = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    first_name = Column(VARCHAR(30), nullable=False)
    last_name = Column(VARCHAR(30), nullable=False)
    phone = Column(VARCHAR(15), nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    
class TypeRelationTutorStudent(Base):
    __tablename__ = "type_relation_tutor_student"
    id_relation = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    relation_type = Column(VARCHAR(50), nullable=False)

class RelStuTutTyp(Base):
    __tablename__ = "rel_stu_tut_typ"
    id_student = Column(INTEGER, ForeignKey('students.id_student'), primary_key=True, index=True, nullable=False)
    id_tutor = Column(INTEGER, ForeignKey('tutors.id_tutor'), primary_key=True, index=True, nullable=False)
    id_relation = Column(INTEGER, ForeignKey('type_relation_tutor_student.id_relation'), primary_key=True, index=True, nullable=False)
    
    student = relationship("Student")
    tutors = relationship("Tutors")
    type_relation_tutor_student = relationship("TypeRelationTutorStudent")

Student.tutors_relation = relationship("RelStuTutTyp", back_populates="student")

Tutors.students_relation = relationship("RelStuTutTyp", back_populates="tutors")
TypeRelationTutorStudent.rel_stu_tut_typ = relationship("RelStuTutTyp", back_populates="type_relation_tutor_student")


class Addressess(Base):
    __tablename__ = "addressess"
    id_address = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    public_road = Column(VARCHAR(50), nullable=False)
    address_number = Column(VARCHAR(50), nullable=True)
    cp = Column(INTEGER(5), nullable=False)
    municipality = Column(VARCHAR(35), nullable=False)
    province = Column(VARCHAR(35), nullable=False)
    country = Column(VARCHAR(35), nullable=False)
    
class Rel_Address_Student(Base):
    __tablename__ = "rel_address_student"
    id_student = Column(INTEGER, ForeignKey('students.id_student'), primary_key=True, index=True, nullable=False)
    id_address = Column(INTEGER, ForeignKey('addressess.id_address'), primary_key=True, index=True, nullable=False)
    
    student = relationship("Student")
    addresses = relationship("Addresses")

# class Student(Base):
#     __tablename__ = "students"
#     id_student = Column(
#         INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False
#     )
#     id_user = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     idalu = Column(INTEGER(10), nullable=False)
#     first_name = Column(VARCHAR(30), nullable=False, index=True) # falta modificar en base de datos
#     last_name = Column(VARCHAR(30), nullable=False)
#     last_name2 = Column(VARCHAR(100), nullable=True)
#     id_course = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     date_of_birth = Column(DATE, nullable=False)
#     place_of_birth = Column(VARCHAR(100), nullable=False)
#     nationality = Column(VARCHAR(30), nullable=False)
#     is_emancipated = Column(TINYINT(1), nullable=False)
#     tutor_family_1 = Column(
#         INTEGER(11), nullable=True
#     )  # falta la relacion y foreign key
#     tutor_family_2 = Column(
#         INTEGER(11), nullable=True
#     )  # falta la relacion y foreign key
#     email = Column(VARCHAR(30), nullable=False)
#     dni = Column(VARCHAR(9), nullable=False)
#     nif = Column(VARCHAR(9), nullable=True)
#     cip = Column(VARCHAR(20), nullable=False)
#     id_address = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     creation_date = Column(DATETIME, nullable=True)
#     update_date = Column(DATETIME, nullable=True)
#     creation_user = Column(INTEGER(11), nullable=True)
#     update_user = Column(INTEGER(11), nullable=True)


# class Users(Base):
#     __tablename__ = "users"
#     id_user = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     username = Column(VARCHAR(30), nullable=False)
#     password = Column(VARCHAR(30), nullable=False)
#     id_role = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     image_path = Column(VARCHAR(30), nullable=True)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False)
#     update_user = Column(INTEGER(10), nullable=False)

# class Tutors(Base):
#     __tablename__ = "tutors"
#     id_tutor = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     first_name = Column(VARCHAR(30), nullable=False)  # falta modificar en base de datos
#     last_name = Column(VARCHAR(30), nullable=False) # falta añadir a base de datos
#     id_relation = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     phone = Column(VARCHAR(9), nullable=False)
#     email = Column(VARCHAR(50), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Tutoring_tracking(Base):
#     __tablename__ = "tutoring_tracking"
#     id_tutoring_tracking = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_tracking = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_tutoring_section = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Tracking(Base):
#     __tablename__ = "tracking_sop"
#     id_tracking = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_user = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_course = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     trackin_date = Column(DATE, nullable=False)
#     notes = Column(VARCHAR(200), nullable=False)
#     id_report = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_contact = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_tutoring_tracking = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Tracking_reports(Base):
#     __tablename__ = "tracking_reports"
#     id_report = Column(INTEGER(11), index=True, nullable=False) # falta la relacion
#     id_tracking = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)  

# class Sop_confidentiality_documents(Base):
#     __tablename__ = "sop_confidentiality_documents"
#     id_document = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     document_type = Column(INTEGER(30), index=True, nullable=False)  # falta la relacion
#     document_path = Column(VARCHAR(50), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Sociogram(Base):
#     __tablename__ = "sociogram"
#     id_sociogram = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     questions = Column(VARCHAR(255), nullable=False)
#     responses = Column(VARCHAR(255), nullable=False)
#     scores = Column(INTEGER(3), nullable=False)
#     teacher_feedback = Column(VARCHAR(255), nullable=False)
#     psychiologist_insight = Column(VARCHAR(255), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Reports_attached(Base):
#     __tablename__ = "reports_attached"
#     id_report = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     report_name = Column(VARCHAR(30), nullable=False)
#     is_confidential = Column(TINYINT(1), nullable=False) # falta corregir nombre a base de datos
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False)
#     update_user = Column(INTEGER(10), nullable=False)

# class Rel_pathology_student(Base):
#     __tablename__ = "rel_pathology_student"
#     id_pathology_student = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_pathology = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     # range = Column(INTEGER(11), nullable=False)
#     note = Column(LONGTEXT, nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False)
#     update_user = Column(INTEGER(10), nullable=False)

# class Pathology(Base):
#     __tablename__ = "pathology"
#     id_pathology = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     pathology_name = Column(VARCHAR(30), nullable=False)
#     note = Column(LONGTEXT, nullable=False) # falta modificar en base de datos
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False)
#     update_user = Column(INTEGER(10), nullable=False)

# class Neurocrib(Base):
#     __tablename__ = "neurocrib"
#     id_neurocrib = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     neurocrib_results = Column(INTEGER(11), nullable=False)
#     document_path = Column(VARCHAR(255), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta añadir a base de datos

# class Games_test(Base):
#     __tablename__ = "games_test"  # falta modificar en base de datos
#     id_game_test = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_game = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     id_test = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     level = Column(INTEGER(11), nullable=False)
#     max_score = Column(INTEGER(11), nullable=False)
#     rounds = Column(INTEGER(11), nullable=False)
#     max_time = Column(INTEGER(11), nullable=False)
#     min_time = Column(INTEGER(11), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos

# class Games_test_tudents(Base):
#     __tablename__ = "games_test_tudents"
#     id_game_test = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     time = Column(INTEGER(11), nullable=False)
#     score = Column(INTEGER(11), nullable=False)
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False)
#     update_user = Column(INTEGER(10), nullable=False)

# class Games(Base):
#     __tablename__ = "games"
#     id_game = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     game_name = Column(VARCHAR(30), nullable=False) # falta modificar en base de datos
#     game_description = Column(LONGTEXT, nullable=False) # falta modificar en base de datos
#     game_path = Column(VARCHAR(255), nullable=False) # falta modificar en base de datos
#     id_category = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos

# class Games_categories(Base):
#     __tablename__ = "games_categories"
#     id_category = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     category_name = Column(VARCHAR(30), nullable=False) # falta modificar en base de datos
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos
#     update_user = Column(INTEGER(10), nullable=False) # falta modificar en base de datos

# class Courses(Base):
#     __tablename__ = "courses"
#     id_course = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     course_name = Column(VARCHAR(20), nullable=False)

# class Addresses(Base):
#     id_address = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     puclic_road = Column(VARCHAR(50), nullable=False)
#     door = Column(INTEGER(10), nullable=False) # falta modificar en base de datos
#     cp = Column(INTEGER(5), nullable=False)
#     municipality = Column(VARCHAR(35), nullable=False)
#     province = Column(VARCHAR(35), nullable=False)
#     country = Column(VARCHAR(35), nullable=False)

# class Contacts_with_professionals(Base):
#     __tablename__ = "contacts_with_professionals"
#     id_contact = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_student = Column(INTEGER(11), index=True, nullable=False)  # falta la relacion
#     professional_name = Column(VARCHAR(30), nullable=False)
#     contact_date = Column(DATE, nullable=False)
#     contact_type = Column(VARCHAR(30), nullable=False)
#     contact_details = Column(LONGTEXT, nullable=False) # falta modificar en base de datos
#     creation_date = Column(DATETIME, nullable=False)
#     update_date = Column(DATETIME, nullable=False)
#     creation_user = Column(INTEGER(11), nullable=False) # falta modificar en base de datos
#     update_user = Column(INTEGER(11), nullable=False) # falta modificar en base de datos

#     # # TEST
#     # id_student = Column(INTEGER(11), primary_key=True, index=True, nullable=False)
#     # name = Column(VARCHAR(255))
#     # last_name = Column(VARCHAR(255))
#     # date_of_birth = Column(DATE)
#     # date_creation = Column(DATE)
#     # is_emancipated = Column(TINYINT(1))
