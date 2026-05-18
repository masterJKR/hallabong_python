#  routers/student_router.py
# 요청 주소처리 (학생 등록/조회)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.student import Student
from schemas.student_schema import StudentCreate, StudentResponse

router = APIRouter()

# 학생 목록 조회 요청
@router.get("/students",response_model=list[StudentResponse])
def get_students(db: Session=Depends(get_db)):
    students = db.query(Student).all()
    return students


# 학생 정보 등록 요청
@router.post("/students",response_model=StudentResponse)
def create_student(student: StudentCreate, 
                   db: Session=Depends(get_db)):
    new_std = Student(
        name=student.name,
        class_n=student.class_n,
        team=student.team
    )
    db.add(new_std)
    db.commit()
    db.refresh(new_std)
    return new_std

