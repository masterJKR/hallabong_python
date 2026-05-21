#  analysis_service.py
import io

import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from models.student import Student
from models.attend import Attend
from models.score import Score

#출석률 그래프
def get_attend_graph_service(db):
    matplotlib.rc("font", family="Malgun Gothic")

    attends = db.query(Attend).all()

    attend_rates= []
    for attend in attends:
        tot_cnt = ( # 학생의 출석률 
            attend.attend + attend.late + attend.absent +
            attend.early_leave
        )
        rate = (attend.attend / tot_cnt ) * 100 # 학생의 출석률
        attend_rates.append(rate)
    
    df = pd.DataFrame({
        "attend_rate":attend_rates
    })
    bins =[0 , 50, 70, 90, 101]
    labels = ["50%미만", "50%~69%", "70%~89%","90%이상"]

    df["attend_range"] = pd.cut(
        df["attend_rate"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False
    )
    attend_counts = df["attend_range"].value_counts().sort_index()

    colors=[
        "#FF5A5A",
        "#FFCD12",
        "#368AFF",
        "#47C83E"
    ]

    legend_labels=[]
    for label, value in zip(labels, attend_counts.values):
        legend_labels.append( f"{label} ({value}명)")

    fig, ax =plt.subplots(figsize=(8,5))

    wedges, texts, autotexts = ax.pie(
        attend_counts.values,
        labels=None,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        wedgeprops={ "width":0.42 , "edgecolor":"white"},
        pctdistance=0.75,
        textprops={
            "color":"white",
            "fontsize":11,
            "fontweight":"bold"
        }
    )

    ax.text(
        0,0,
        f"전체\n{len(attends)}명",
        ha="center",
        va="center",
        fontsize=16 , fontweight="bold", color="#000000"
    )
    ax.set_title("출석률 분포", fontsize=16, fontweight="bold",pad=20)

    ax.legend(
        wedges[::-1], legend_labels[::-1], loc="center left",
        bbox_to_anchor=(1.05 , 0.5 ), 
        frameon =False,
        fontsize=11,
        labelspacing=1.5
    )
    # bbox_to_anchor=(x,y)
    # 범례좌표- x=0(그래프왼쪽) , x=1(그래프 오른쪽)
    #          y=0 (그래프 아래) , y=1(그래프 위)
    fig.tight_layout()
    img = io.BytesIO()
    fig.savefig(img, format="png",dpi=150, bbox_inches="tight")
    img.seek(0)
    plt.close(fig)
    return StreamingResponse( img, media_type="image/png")



#성적 그래프
def get_score_graph_service(db):
    matplotlib.rc("font", family="Malgun Gothic")

    plt.rcParams["axes.unicode_minus"]=False  # 음수 표현

    scores = db.query(Score).all()

    avg_scores = []
    for score in scores:
        avg = (  # 학생 한명의 평균값
            score.python_score + score.numpy_score +
            score.pandas_score + score.java_score +
            score.project_score
        )/5
        avg_scores.append(avg)
    df = pd.DataFrame( {
        "avg_score" : avg_scores
    })
    bins = [ 0, 50, 60, 70, 80, 90, 101]
    labels=["0~50점", "50~60점","60~70점","70~80점",
            "80~90점","90~100점"]
    df["score_range"] = pd.cut(
        df["avg_score"],
        bins=bins,
        labels=labels,
        include_lowest=True,
        right=False
    )

    score_counts = df["score_range"].value_counts().sort_index()

    fig, ax = plt.subplots( figsize= (8,5) )

    bars = ax.bar(
        score_counts.index.astype(str),
        score_counts.values,
        width=0.5
    )
    ax.set_title("성적 분포 그래프",fontsize=16, 
              fontweight="bold", pad=20)
    ax.set_ylabel("학생 수(명)",rotation=0 , labelpad=40, fontsize=11)
    ax.grid( axis="y",alpha=0.25)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2, 
            height+ 0.1,
            int(height),
            ha="center",
            fontsize=11
        )

    fig.tight_layout()
    img = io.BytesIO()
    fig.savefig( img, format="png",dpi=150, bbox_inches="tight")

    img.seek(0)
    plt.close(fig)
    return StreamingResponse( img, media_type="image/png")


#위험, 우수 학생 
def get_student_status_service(db):
    students = db.query(Student).all()

    danger_std=[]
    excellent_std=[]

    for std in students:
        score = db.query(Score).filter(Score.student_id == std.id)\
                    .first()
        attend = db.query(Attend).filter(Attend.student_id == std.id)\
                    .first()
        if score is None: continue
        if attend is None : continue

        avg = (  # 학생 한명의 평균값
            score.python_score + score.numpy_score +
            score.pandas_score + score.java_score +
            score.project_score
        )/5

        tot_cnt = ( # 학생의 출석률 
            attend.attend + attend.late + attend.absent +
            attend.early_leave
        )
        rate = (attend.attend / tot_cnt ) * 100

        data = { 
            "name" : std.name,
            "avg_score":avg,
            "attend_rate":rate
        }
        if ( avg < 60 or rate < 70 ) : # 관리 학생 분류
            data["status"]="관리필요"
            danger_std.append(data)
        elif ( avg >=90 and rate>=90): # 우수 학생 분류
            data["status"] = "우수"
            excellent_std.append(data)

    return { 
        "danger_std":danger_std,
        "excellent_std":excellent_std
    }


# 반전체 통계  - ClassSummaryPage
def get_class_summary(db):
    total_student = db.query(Student).count()
    if total_student ==0:
        raise HTTPException(
            status_code=404,
            message="등록된 학생이 없습니다."
        )
    # 전체 성적 조회
    scores = db.query(Score).all()

    # 전체 출석 조회
    attends = db.query(Attend).all()

    temp_avg_score = 0  # 전체 평균 계산위한 임시변수

    for score in scores:
        avg = (
            score.python_score + score.numpy_score +
            score.pandas_score + score.java_score +
            score.project_score
        )/5
        temp_avg_score += avg
    # 전체 평균값
    avg_score = temp_avg_score / total_student

    #과목별 최고점 최저점
    python_scores = [ score.python_score for score in scores ] 
    numpy_scores = [ score.numpy_score for score in scores ] 
    pandas_scores = [ score.pandas_score for score in scores ]
    java_scores = [ score.java_score for score in scores ]  
    project_scores = [ score.project_score for score in scores ]

    # 전체 출석률 
    total_rate = 0.0

    for att in attends:
        tot_cnt = (
            att.attend + att.late + att.absent +
            att.early_leave
        )
        rate = (att.attend / tot_cnt ) * 100
        total_rate += rate
    avg_attend_rate = round( 
        total_rate/total_student , 2
    )

    return { 
        "total_student":total_student,
        "avg_score":avg_score,
        "avg_attend_rate":avg_attend_rate,
        "python_max":max(python_scores),
        "python_min":min(python_scores),
        "numpy_max":max(numpy_scores),
        "numpy_min":min(numpy_scores),
        "pandas_max":max(pandas_scores),
        "pandas_min":min(pandas_scores),
        "java_max":max(java_scores),
        "java_min":min(java_scores),
        "project_max":max(project_scores),
        "project_min":min(project_scores)
    }

