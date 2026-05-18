#  models/student.py

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.db import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50) , nullable=False)
    class_n = Column(String(100))
    team = Column(String(100))
    create_at = Column(DateTime, default=datetime.now)