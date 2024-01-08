import strawberry
from strawberry.fastapi import GraphQLRouter
from ..dashboard.models.models import Student, StudentRead
from fastapi import Depends
from typing import List
from sqlmodel import Session, select
from app.database import get_session, engine
from typing import Optional
from datetime import date, datetime

@strawberry.experimental.pydantic.type(
    
    model=Student, 
    fields=[
        "id_student",
        "id_user",
        "first_name",
        "last_name1",
        "last_name2",
        "date_of_birth",
        "place_of_birth",
        "is_emancipated",
        "email",
        "dni",
        "id_address",
        "created_by",
        "updated_by",
        "created_at",
        "updated_at"]
    )
class StudentType:
    pass


@strawberry.type
class StudentReadType:
    id_student: Optional[int] = None
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

def get_students() -> List[Student]:
    with Session(engine) as session:
        heroes = session.exec(select(Student)).all()
        return heroes

def get_student(id: int) -> Student:
    with Session(engine) as session:
        heroes = session.get(Student, id)
        return heroes

@strawberry.type
class Query:
    @strawberry.field
    def students(self) -> List[StudentReadType]:
        return get_students()
    
    @strawberry.field
    def student(self, id: int) -> StudentReadType:
        return get_student(id)
    
    
# @strawberry.type
# class User:
#     name: str
#     age: int


# @strawberry.type
# class Query:
#     @strawberry.field
#     def user(self) -> User:
#         return User(name="Patrick", age=100)



    
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)