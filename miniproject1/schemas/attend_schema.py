from pydantic import BaseModel
from datetime import datetime

class AttendCreate(BaseModel):
    student_id: int
    attend:int
    late:int
    absent:int
    early_leave:int

class AttendResponse(BaseModel):
    id: int
    student_id:int
    student_name:str
    attend:int
    late:int
    absent:int
    early_leave:int
    total_count:int
    attend_rate:float

    class Config:
        from_attributes=True