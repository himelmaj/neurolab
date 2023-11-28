from fastapi import FastAPI
from database import ping_database

app = FastAPI()


@app.get("/ping")
async def root():
    return {"message": "Ping Success!"}

@app.get("/database")
async def read_root():
   return ping_database()
