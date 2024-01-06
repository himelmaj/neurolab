from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import date, datetime

if TYPE_CHECKING:
    from student_model import Student, StudentRead
    
class StudentTutor(SQLModel, table=True):    
    id_student: Optional[int] = Field(default=None, primary_key=True, index=True, foreign_key="student.id_student")
    id_tutor: Optional[int] = Field(default=None, primary_key=True, index=True, foreign_key="tutor.id_tutor")

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
    students: List["Student"] = Relationship(back_populates="tutor")
    
class TutorRead(TutorBase):
    id_tutor: int
    
class TutorCreate(TutorBase):
    pass

class TutorReadWithStudents(TutorRead):
    students: List["StudentRead"] = []