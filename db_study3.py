#  db_study3.py

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="krkr",
    password="1234",
    database="krkr",
    charset="utf8"
)

cur = conn.cursor()

#  cur.execute( 쿼리문 )
#  conn.commit()

cur.execute("select * from item where item_qa >= %s",
            (30,))

rows = cur.fetchall()
for row in rows:
    print(row)

