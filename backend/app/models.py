from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR, DATE
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = "students"
    # id_student = Column(INTEGER(11), primary_key=True, index=True, autoincrement=True, nullable=False)
    # id_user = Column(INTEGER(11),ForeignKey("users.id_user"), index=True, nullable=False) #falta la relacion
    # idalu = Column(INTEGER(10),  nullable=False)
    # name = Column(String(length=30), nullable=False, index=True)
    # last_name = Column(String(length=30), nullable=False, index=True)
    # last_name2 = Column(String(length=100), nullable=True)
    # id_course = Column(INTEGER(11), ForeignKey("courses.id_course"), index=True, nullable=False) #falta la relacion
    # date_of_birth = Column(DATE, nullable=False)
    # place_of_birth = Column(String(length=100), nullable=False)
    # nationality = Column(String(length=30), nullable=False)
    # is_emancipated = Column(TINYINT(1), nullable=False)
    # tutor_family_1 = Column(INTEGER(11), nullable=True) # falta la relacion y foreign key
    # tutor_family_2 = Column(INTEGER(11), nullable=True) # falta la relacion y foreign key
    # email = Column(String(length=30), nullable=False)
    # dni = Column(String(length=9), nullable=False)
    # nif = Column(String(length=9), nullable=True)
    # cip = Column(String(length=20), nullable=False)
    # id_address = Column(INTEGER(11), ForeignKey("addresses.id_address"), index=True, nullable=False) #falta la relacion
    # creation_date = Column(DATE, nullable=True)
    # update_date = Column(DATE, nullable=True)
    # creation_user = Column(INTEGER(11), nullable=True)
    # update_user = Column(INTEGER(11), nullable=True)

    
    
    
    # TEST
    id_student = Column(INTEGER(11), primary_key=True, index=True, nullable=False)
    name = Column(VARCHAR(255))
    last_name = Column(VARCHAR(255))
    date_of_birth = Column(DATE)
    date_creation = Column(DATE)
    is_emancipated = Column(TINYINT(1))