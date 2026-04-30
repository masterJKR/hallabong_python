# db_study2.py

import sqlite3
import random

# 테이블 접속
def db_connect():
    conn=sqlite3.connect("test.db")
    cur = conn.cursor()
    return conn,cur


# 테이블 생성
def create_table():
    conn, cur = db_connect()
    cur.execute("""
        create table board(
            id integer primary key autoincrement,
            title text,
            content text,
            writer integer
                )
    """)
    conn.commit()
    conn.close()


# 데이터 입력
def save():
    conn , cur =db_connect()
    title = ["제목1","내일부터","5일","쉰다","애들엄마 처가집간다."]
    content =["내용1","애들은","나혼자","본다"]

    for i in range(5):
        cur.execute("insert into board (title,content,writer) values(?,?,?)",
                (random.choice(title) , random.choice(content), random.randint(1,3)) )
        conn.commit()

    conn.close()

#테이블 전체 조회 
def findAll():
    conn , cur = db_connect()
    conn.row_factory = sqlite3.Row  # 테이블의 데이터를 딕셔너리로 받기위해 필요

    cur = conn.cursor()

    cur.execute("select * from board")
    data = []
    for row in cur:
        data.append( dict(row) )
    return data


# 테이블 조건 조회
def find_by_writer(writer_id):
    conn , cur = db_connect()

    cur.execute("select b.* from board b join info i on b.writer = i.id where i.id=?",
                (writer_id,) )
    rows= cur.fetchall()
    for row in rows:
        print(row)


find_by_writer(1)

#create_table()
#save()
data = findAll()
print(data)