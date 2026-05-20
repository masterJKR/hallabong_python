from fastapi import HTTPException

from models.attend import Attend
from models.student import Student
from schemas.attend_schema import AttendResponse


def create_attend_db(attendData, db):
    student = db.query(Student)\
    .filter(Student.id == attendData.student_id)\
    .first()

    if student is None:
        raise HTTPException(status_code=404,message="학생정보 없음")

    new_attend = Attend(
        student_id = attendData.student_id,
        attend = attendData.attend,
        late = attendData.late,
        absent = attendData.absent,
        early_leave = attendData.early_leave
    )
    db.add(new_attend)
    db.commit()
    db.refresh(new_attend)



def get_attend_list(db):
    attend_list = db.query(Attend, Student)\
    .join(Student, Attend.student_id == Student.id)\
    .all()
    result = []

    for att, std in attend_list:
        attend_rate ,total_count = calc_attend_rate(
            att.attend, att.late,att.absent, att.early_leave
        )

        result.append( AttendResponse(
            id=att.id,
            student_id=std.id,
            student_name=std.name,
            attend=att.attend,
            late=att.late,
            absent=att.absent,
            early_leave=att.early_leave,
            total_count=total_count,
            attend_rate=attend_rate
        ))
    return result


def calc_attend_rate(attend, late, absent, early_leave):
    total_count = attend + (late//3) + absent+ (early_leave//3)
    if total_count == 0: return 0

    return round((attend / total_count) *100,1) , total_count