from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
# from app.router import router
from .src.dashboard.routers.students_router import router as students_router
from .src.dashboard.routers.tutors_router import router as tutors_router
from fastapi_pagination import add_pagination
from .database import init_db
app = FastAPI(
    title="Neurolab Monlau API",
    description="Neurolab API",)

origins = [
    config('FRONTEND_URL'),
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def read_main():
    return {"message": "Welcome to Neurolab API"}

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(students_router)
app.include_router(tutors_router)
add_pagination(app)

