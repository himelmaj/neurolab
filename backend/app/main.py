from fastapi import FastAPI
from crud import router

app = FastAPI()

app.include_router(router)
