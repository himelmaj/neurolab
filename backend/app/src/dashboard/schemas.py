from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class StudentBase(BaseModel):
    student_id : int = Field(alias="id_student")
    idalu : int = Field(alias="idalu")
    first_name : str = Field(alias="first_name")
    last_name : str = Field(alias="last_name")
    date_of_birth : date = Field(alias="date_of_birth")
    is_emancipated : bool = Field(alias="is_emancipated")
    email : str = Field(alias="email")
    nif : str = Field(alias="nif")
    cip : str = Field(alias="cip")
    
    class Config:
        from_attributes = True
        
class TutorBase(BaseModel):
    tutor_id : int = Field(alias="id_tutor")
    id_relation : int = Field(alias="id_relation")
    first_name : str = Field(alias="first_name")
    last_name : str = Field(alias="last_name")
    phone : str = Field(alias="phone")
    email : str = Field(alias="email")
    
    class Config:
        from_attributes = True
    
class StudentSchema(StudentBase):
    tutors : List[TutorBase]

class TutorSchema(TutorBase):
    students : List[StudentBase]