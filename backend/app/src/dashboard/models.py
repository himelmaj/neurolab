from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR, DATE, DATETIME, LONGTEXT, BOOLEAN
from sqlalchemy.orm import relationship
from app.database import Base


rel_students_tutors = Table('rel_students_tutors', Base.metadata,
    Column('id_student', INTEGER, ForeignKey('students.id_student'), primary_key=True, nullable=False),
    Column('id_tutor', INTEGER, ForeignKey('tutors.id_tutor'), primary_key=True, nullable=False)
)

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
    tutors = relationship("Tutor", secondary="rel_students_tutors", back_populates="students")
    
class Tutor(Base):
    __tablename__ = "tutors"
    
    id_tutor = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    id_relation = Column(INTEGER, ForeignKey('type_relation_tutor_student.id_relation'), index=True, nullable=False)
    first_name = Column(VARCHAR(30), nullable=False)
    last_name = Column(VARCHAR(30), nullable=False)
    phone = Column(VARCHAR(15), nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    students = relationship("Student", secondary="rel_students_tutors", back_populates="tutors")
    
    type_relation_tutor_student = relationship("TypeRelationTutorStudent")
    
class TypeRelationTutorStudent(Base):
    __tablename__ = "type_relation_tutor_student"
    id_relation = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
    relation_type = Column(VARCHAR(50), nullable=False)

