# matplotlib_test.py

'''
    125번  png와 json 파일을 사용하여  다음을 만들어 보세요

    이미지안에서  차량의 크기가 가장 큰  차  와
    크기가  세번째로 큰 차 를  바운딩박스로 표시해주세요
    가장큰차의 바운딩 박스 테두리 색은  red
    세번째로 큰차의 바운딩 박스 테두리색은  yellow

'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import json

with open('18396708_frame_125.json','r', encoding='utf-8') as f:
    data = json.load(f)

annotations = data['frames']['annotations']

area = list()
for ann in annotations:
    label= ann['label']
    area.append( (label['x'], label['y']
                  ,  label['width'], label['height']) )

# 너비큰순으로 정렬
area.sort(reverse=True, key=lambda x : x[2] * x[3])

img = plt.imread('18396708_frame_125.png')

plt.imshow(img)
ax = plt.gca()
x ,y ,width, height = area[0]
box=patches.Rectangle(
        (x,y) ,   #  시작 좌표
        width,  # 너비 크기
        height,  # 높이 크기
        fill=False, # 박스 내부 색 채우기 여부
        edgecolor='red' ,  # 박스 테두리 색
        linewidth=2  # 테두리 선 굵기
    )
ax.add_patch(box)

x ,y ,width, height = area[2]
box=patches.Rectangle(
        (x,y) ,   #  시작 좌표
        width,  # 너비 크기
        height,  # 높이 크기
        fill=False, # 박스 내부 색 채우기 여부
        edgecolor='yellow' ,  # 박스 테두리 색
        linewidth=2  # 테두리 선 굵기
    )
ax.add_patch(box)
plt.show()