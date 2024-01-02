from sqlalchemy import Column, Date, Integer, String, ForeignKey, Table
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR, DATE, DATETIME, LONGTEXT, BOOLEAN
from sqlalchemy.orm import relationship
from app.database import Base
# from app.src.tutors.models import Tutor

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
    # tutors = relationship("Tutor", secondary="rel_students_tutors", back_populates="students")
    
    
    
