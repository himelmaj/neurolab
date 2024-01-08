from decouple import config
from sqlmodel import Session, create_engine, SQLModel

DB_URL = config('DB2')
engine = create_engine(DB_URL, echo=True)

def init_db():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")

def close_db_connection():
    try:
        engine.dispose()
        print("Database connection closed.")
    except Exception as e:
        print(f"Error closing database connection: {e}")   

def get_session():
    with Session(engine) as session:
        try:
            yield session
        except Exception as e:
            print(f"Error during database session: {e}")
            session.rollback()
            raise
        finally:
            session.close()
            