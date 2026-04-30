#json_test2.py

import json

# 화면에 자동차가  몇대가 있냐  
with open("file/18396710_frame_127.json" , "r", encoding="utf-8") as f:
    data = json.load(f)

anno = data["frames"]["annotations"]

print( "차량 몇대 : " , len(anno) )

anno_value = dict()

for ann in anno:
    val = ann["category"]["attributes"][0]["value"]
    if val not in anno_value:
        anno_value[val] = 0
    anno_value[val] += 1

print( anno_value )

# 가장 큰 객체 찾기

max_area = 0
big_object = None

for ann in anno:
    area = ann["label"]["width"] * ann["label"]["height"]

    if area > max_area:
        max_area = area
        big_object = ann

print("가장 큰 객체 : ", big_object["label"]["x"] , big_object["label"]["y"])
