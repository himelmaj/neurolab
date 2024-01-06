from decouple import config
from sqlmodel import Session, create_engine, SQLModel

db_url = config('DB3')
connect_args = {"check_same_thread": False}
engine = create_engine(db_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session