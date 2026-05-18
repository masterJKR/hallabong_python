#  폴더 - miniproject1  
#  새파일 - main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import Base, engine
from models import student
from schemas import student_schema
from routers import student_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router.router)