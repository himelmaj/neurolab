from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from decouple import config
from .utils import startup, shutdown, Lifespans
from .src.dashboard.routers.students_router import router as students_router
from .src.dashboard.routers.tutors_router import router as tutors_router
from .src.dashboard.routers.courses_router import router as courses_router
from .src.graphql.graphql import graphql_app



app = FastAPI(
    title="Neurolab Monlau API",
    description="Neurolab API",
    lifespan=Lifespans([startup, shutdown]),
)


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

app.include_router(students_router)
app.include_router(tutors_router)
app.include_router(courses_router)
app.include_router(graphql_app, prefix="/graphql")

add_pagination(app)

