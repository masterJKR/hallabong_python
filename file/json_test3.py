#json_test3.py

'''
18396595_frame_12.json 에서   사람을 찾고  사람의 좌표를 출력하세요
'''

import json

with open("file/18396595_frame_12.json", "r", encoding="utf-8") as f:
    data = json.load(f)

annotations = data["frames"]["annotations"]

for ann in annotations:
    if ann["category"]["code"] =="person":
        x = ann["label"]["x"]
        y = ann["label"]["y"]

        print(f"사람 발견 했다!!  x={x} , y={y} ")
