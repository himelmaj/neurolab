from fastapi import FastAPI
from crud import router
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config('FRONTEND_URL'),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)
