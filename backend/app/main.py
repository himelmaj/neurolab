from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
# from app.router import router
from app.src.students.router import router as students_router

app = FastAPI(
    title="Neurolab Monlau API",
    description="Neurolab API",
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
async def load_root():
    return {"message": "Welcome to Neurolab API"}
    
# app.include_router(router)
app.include_router(students_router)

