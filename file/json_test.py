#json_test.py

import json

info =[ 
    {
    "name":"김유신",
    "age":35,
    "addr":"경주"
    },
    { "name":"이순신", "age": 50, "addr":"여수"}

]
with open("file/info.json", "w", encoding="utf-8") as f:
    json.dump(info , f, ensure_ascii=False, indent=4)


# json 읽기
with open("file/info.json", "r", encoding="utf-8") as f:
    member = json.load(f)

for user in member:
    print(user["name"] , user["age"])

member.append( {"name":"문익점","age":25,"addr":"개경"}  )

with open("file/info.json", "w", encoding="utf-8") as f:
    json.dump(member , f, ensure_ascii=False, indent=4)


'''
    파이썬과  json  
    dict   -   object
    list   -   array
    str    -   string
    int,float  -  number
    True    -   true
    False   -  false
    None    -   null

    

'''
