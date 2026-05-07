#  matplotlib_study4.py

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import json
# json에서  car, truck, person의 갯수 그래프로 그리기
with open('18396603_frame_20.json','r', encoding='utf-8') as f:
    data = json.load(f)

# car, truck, person 객체별로 몇개?
counts = { 'car' :0 , 'truck':0 , 'person':0 }

for ann in data['frames']['annotations']:
    code = ann['category']['code']
    if code == 'vehicle':
        value = ann['category']['attributes'][0]['value']
        counts[value] += 1
    elif code =='person':
        counts['person'] += 1

label = list(counts.keys())
values = list(counts.values())
plt.bar(label, values, color=['blue','red','green'])
plt.ylim(0, max(values) + 1 )
plt.show()




# 이미지의 색 분포 그래프 그리기

# img = Image.open('18396603_frame_20.png')
#
# gray = img.convert('L') # 그레이 스케일 변환 - RGB읽으려면 cv 필요
#
# gray_arr = np.array(gray) # 배열로 변환
#
# # 픽셀 값 분포 히스토그램 그래프 만들기
# plt.figure(figsize=(10,4))
#
# # 이미지 밝기 분포를 히스토그램으로 보여주기
# # ravel() 은  2차원 이미지를 1차원으로 제공하기 위해 사용
# #  히스토그램은 2차원 배열이 아닌 1차원배열 형태가 필요하기 때문에
# #  bins=256  은 0~255까지  256칸으로 나누기 위한것 (그래야 분포를 자세히볼수있다.)
# plt.hist(gray_arr.ravel(), bins=256 , color='gray')
#
# plt.title('Histogram')
# plt.xlim([0,256])
# plt.show()



