#  score.py

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from database.db import Base

class Score(Base):
    __tablename__ = "score"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    python_score = Column(Integer)
    numpy_score = Column(Integer)
    pandas_score = Column(Integer)
    java_score = Column(Integer)
    project_score = Column(Integer)
    create_at = Column(DateTime, default=datetime.now)