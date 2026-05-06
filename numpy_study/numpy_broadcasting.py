#  numpy_broadcasting.py

import numpy as np

img = np.array([
    [10,20,30],
    [40,50,60]
])
print( img + 10 )
print( img  - 20 )

v = np.array( [10,20,30] )

print( img + v )

# 열방향 브로드 캐스팅
v2 = np.array([[100],[200]]) # 2차원 배열
print( img + v2)

# 2행 3열  +  1차원 (데이터 3개)
# 2행 3열 +  2차원 (2행 1열)
#  (5,4,3) +  (3, )

#  (2,3)  +  (2,2)

v3 = np.array([[100,10],[200,20]])
v4=np.array([[1,2],[3,4]])
print(v3 + v4)