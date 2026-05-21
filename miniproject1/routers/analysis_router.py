#  analysis_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from service.analysis_service import ( 
    get_class_summary, get_student_status_service ,
     get_score_graph_service , get_attend_graph_service,
      get_graph_summary_service , create_report_service )

router = APIRouter()

@router.get("/analysis/report")
def create_report( db:Session=Depends(get_db)):
    return create_report_service(db)


@router.get("/analysis/graph-summary")
def get_graph_summary(db:Session = Depends(get_db)):
    return get_graph_summary_service(db)

@router.get("/analysis/attend-graph")
def get_attned_graph(db:Session = Depends(get_db)):
    return get_attend_graph_service(db)


@router.get("/analysis/score-graph")
def get_score_graph(db:Session = Depends(get_db)):
    return get_score_graph_service(db)


@router.get("/analysis/student-status")
def get_student_status(db: Session = Depends(get_db)):
    return get_student_status_service(db)


@router.get("/analysis/class-summary")
def get_class_summary_res(db:Session = Depends(get_db)):
    return get_class_summary(db)