# from fastapi import FastAPI
# from database import ping_database



# @app.get("/ping")
# async def root():
#     return {"message": "Ping Success!"}



from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models, schemas
from database import ping_database



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/students/")
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

@app.get("/database")
async def read_root():
   return ping_database()