from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from service.attend_service import (get_attend_list, create_attend_db)
from schemas.attend_schema import AttendCreate

router = APIRouter()

@router.post("/attend")
def create_attend(attendData:AttendCreate , db: Session=Depends(get_db)):
    create_attend_db(attendData, db)

@router.get("/attend")
def get_attend( db: Session=Depends(get_db)):
    return get_attend_list(db)