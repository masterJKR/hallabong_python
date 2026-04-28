from data import db as _db


def login_process(id,pw):
    uid, upw = _db.find_by_id(id)
    if uid==id and upw == pw:
        return "로그인 성공했습니다."
    else:
        return "아이디 또는 비밀번호가 잘못되었습니다."