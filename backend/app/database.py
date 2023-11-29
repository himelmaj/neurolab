from decouple import config
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(config('DATABASE_TEST2'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def ping_database():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
            return {"message": "Versión de la base de datos", "data": result.scalar()}
    except Exception as e:
        return {"error": f"Error al conectar a la base de datos: {str(e)}"}