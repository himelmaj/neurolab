from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os
from decouple import config
from app.routes import router
from app.src.dashboard.router import dashboard_router

app = FastAPI(
    prefix="/api",
    tags=["api"],
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

@app.api_route("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK, methods=['GET', 'HEAD'])
async def load_root():
    templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
    with open(os.path.join(templates_dir, "index.html"), "r") as file:
        return file.read()
    
app.include_router(router)
app.include_router(dashboard_router)

