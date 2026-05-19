#  score_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from service.score_service import (get_score_list ,create_score_service)
from schemas.score_schema import (ScoreCreate, ScoreResponse)

router = APIRouter()

# 성적 등록
@router.post("/scores")
def create_score(score:ScoreCreate, db: Session=Depends(get_db)):
    create_score_service(score, db)



# 성적 조회
@router.get("/scores")
def get_score(db:Session=Depends(get_db)):
    
    return get_score_list(db)

