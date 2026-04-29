#party.py

import csv

party_list = list()  # csv 데이터 저장할 리스트

with open("file/대전축제.csv" , "r" ) as f:
    data = csv.reader(f)

    header = next(data)  # 대전축제csv의 필드명 header에 리스트로저장

    for row in data:
        temp_dic = dict() # 빈 딕셔너리 - 하나의 축제에 대하여 저장
        for i, v in enumerate(row):
            temp_dic[header[i]] = v
            #temp_dic.setdefault("key이름", 값)
        party_list.append(temp_dic)


# 축제 검색 하기
#  입력한 키워드가  포함 되어있는 축제명을 찾는다. 
#  검색에 제외할 키 - 문의전화, 주최, 주관

keyword = input("검색 입력 : ").strip() # 공백 제거(좌우)

result = set() # 검색 결과 축제명이 저장될 set

for row in party_list:
    for k,v in row.items():
        if k in ["주최","주관","문의전화"]:
            continue
        if keyword in v:
            result.add(  row["축제명"]  ) 

print( result )