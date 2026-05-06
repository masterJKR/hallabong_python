import numpy as np
#bright_test.py
# 흑백 사진에서  밝은 영역이 어디인지  찾아서 표시하시오
# 어두운 - 0 ,  밝은 -255
#  200 이상인 영역을 찾기
img = np.array([
    [10, 20, 30, 40, 50],
    [60, 200, 210, 70, 80],
    [90, 220, 255, 100, 110],
    [120, 130, 140, 150, 160]
])




print("이미지 전체 값 ")
print( img )


print("밝은 이미지 영역 ")
bri = img>=200
print(bri)
# 밝은 영역을 더  밝게 !
copy_img = img.copy()  # 원본데이터 유지를 위한 복사
copy_img[copy_img>=200] = 255
print(copy_img)

# 밝은영역이 몇군데??
count = np.sum(copy_img == 255)
print(count)
#밝은영역 좌표는??
pos = np.argwhere(copy_img == 255)
print("좌표는? ",pos)

# 밝은영역위치의 값만 추출하기
rows = pos[:,0]
cols = pos[:,1]
print("행 : " ,rows)
print("열 :" , cols)

min_row = rows.min() # 행번호의 최소값
max_row = rows.max() # 행번호의 최대값
min_col = cols.min() # 열번호의 최소값
max_col = cols.max() # 열번호의 최대값
# img[1:2, 1:2]
find = img[min_row : max_row + 1, min_col :max_col + 1]
print(find)