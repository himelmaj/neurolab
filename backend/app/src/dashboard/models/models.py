from typing import List, Optional
from sqlmodel import Field, Relationship, Session, SQLModel
from datetime import date, datetime

class StudentTutor(SQLModel, table=True):
    __tablename__ = "student_tutor" 
    id_student: Optional[int] = Field(default=None, primary_key=True, index=True, foreign_key="student.id_student")
    id_tutor: Optional[int] = Field(default=None, primary_key=True, index=True, foreign_key="tutor.id_tutor")
   
    
class StudentBase(SQLModel):
    id_user: Optional[int] = Field(default=None, index=True)
    first_name: str = Field(default=None, max_length=30)
    last_name1: str = Field(default=None, max_length=50)
    last_name2: Optional[str] = Field(default=None, max_length=50)
    date_of_birth: date = Field(default=None)
    place_of_birth: str = Field(default=None, max_length=50)
    is_emancipated: bool = Field(default=None)
    email: str = Field(default=None, max_length=255)
    dni: str = Field(default=None, max_length=9)
    id_address: Optional[int] = Field(default=None, index=True)
    created_by: Optional[int] = Field(default=None, index=True)
    updated_by: Optional[int] = Field(default=None, index=True)
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    
class Student(StudentBase, table=True):
    id_student: Optional[int] = Field(default=None, primary_key=True, index=True)
    tutors: List["Tutor"] = Relationship(back_populates="students", link_model=StudentTutor)
    
class StudentRead(StudentBase):
    id_student: int
    
class StudentCreate(StudentBase):
    pass

class StudentUpdate(SQLModel):
    id_user: Optional[int] = None
    first_name: Optional[str] = None
    last_name1: Optional[str] = None
    last_name2: Optional[str] = None
    date_of_birth: Optional[date] = None
    place_of_birth: Optional[str] = None
    is_emancipated: Optional[bool] = None
    email: Optional[str] = None
    dni: Optional[str] = None
    id_address: Optional[int] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TutorBase(SQLModel):
    id_user: Optional[int] = Field(default=None, index=True)
    id_relation: Optional[int] = Field(default=None, index=True)
    first_name: str = Field(default=None, max_length=30)
    last_name1: str = Field(default=None, max_length=50)
    last_name2: Optional[str] = Field(default=None, max_length=50)
    phone: str = Field(default=None, max_length=15)
    email: str = Field(default=None, max_length=255)
    created_by: Optional[int] = Field(default=None, index=True)
    updated_by: Optional[int] = Field(default=None, index=True)
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    
class Tutor(TutorBase, table=True):
    id_tutor: Optional[int] = Field(default=None, primary_key=True, index=True)
    students: List["Student"] = Relationship(back_populates="tutors", link_model=StudentTutor)
    
class TutorRead(TutorBase):
    id_tutor: int
    
class TutorCreate(TutorBase):
    pass

class TutorUpdate(SQLModel):
    id_user: Optional[int] = None
    id_relation: Optional[int] = None
    first_name: Optional[str] = None
    last_name1: Optional[str] = None
    last_name2: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class StudentReadWithTutors(StudentRead):
    tutors: List[TutorRead] = []
    
class TutorReadWithStudents(TutorRead):
    students: List[StudentRead] = []