from decouple import config
import models
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends

engine = create_engine(config('DATABASE_TEST2'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

async def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = await db.query(models.Student).offset(skip).limit(limit).all()
    return students