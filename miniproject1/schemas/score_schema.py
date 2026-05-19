#  score_schema.py

from pydantic import BaseModel
from datetime import datetime

class ScoreCreate(BaseModel):
    student_id: int
    python_score:int
    numpy_score:int
    pandas_score:int
    java_score:int
    project_score:int

class ScoreResponse(BaseModel):
    id: int
    student_id:int
    student_name:str
    python_score:int
    numpy_score:int
    pandas_score:int
    java_score:int
    project_score:int
    total_score:int
    avg_score:float
    create_at:datetime

    class Config:
        from_attributes=True