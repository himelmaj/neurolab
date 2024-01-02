# from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table
# from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR, DATE, DATETIME, LONGTEXT, BOOLEAN
# from sqlalchemy.orm import relationship
# from app.database import Base
# from app.src.students.models import Student
# from app.models import rel_students_tutors

# class Tutor(Base):
#     __tablename__ = "tutors"
    
#     id_tutor = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
#     id_relation = Column(INTEGER, ForeignKey('type_relation_tutor_student.id_relation'), index=True, nullable=False)
#     first_name = Column(VARCHAR(30), nullable=False)
#     last_name = Column(VARCHAR(30), nullable=False)
#     phone = Column(VARCHAR(15), nullable=False)
#     email = Column(VARCHAR(50), nullable=False)
#     students = relationship("Student", secondary="rel_students_tutors", back_populates="tutors")
    
#     type_relation_tutor_student = relationship("TypeRelationTutorStudent")
    
# class TypeRelationTutorStudent(Base):
#     __tablename__ = "type_relation_tutor_student"
#     id_relation = Column(INTEGER, primary_key=True, index=True, autoincrement=True, nullable=False)
#     relation_type = Column(VARCHAR(50), nullable=False)