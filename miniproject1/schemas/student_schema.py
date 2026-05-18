#  schemas/student_schema.py
#  학생 데이터 응답, 요청 구조 정의 

from pydantic import BaseModel
from datetime import datetime

# 학생 등록 데이터 구조
class StudentCreate(BaseModel):
    name: str
    class_n: str
    team: str

# 학생 목록 데이터 구조
class StudentResponse(BaseModel):
    id: int
    name: str
    class_n: str
    team: str
    create_at: datetime

    class Config:
        from_attributes = True