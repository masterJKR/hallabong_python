#  numpy_study2.py

import numpy as np

# 배열 자동 생성
a = [ num for num in range(1,11,2) ]
print(a)

# arange(시작, 끝, 증가값)
arr = np.arange(1,11,2)  # 배열 자동생성 : arange( 숫자)
print(arr)

arr = np.arange(1,16)  #  1부터 15까지
arr2 = arr.reshape(3,5)  #  3행 5열의 2차원배열로 변환
# 차원 변경시  데이터 개수가 일치해야한다.
print(arr2)

arr3 = arr.reshape(-1, 3 ) # -1은 numpy가 알아서 계산해준다.
# 변환 하고자 하는 차원의 행열 중 한가지는 정해줘야한다.
print(arr3)

dim1 = np.arange(24)
dim3 = dim1.reshape(3, -1 ,2)  # x+y+3 = 24
print(dim3)
dim_origin = dim3.reshape(dim3.size)
print(dim_origin)

# 0으로 채워진 배열 생성
# .zeros() 의 기본 타입은 실수형이다.
zero_arr = np.zeros((3,3) , dtype=int) # 정수형으로 만들려면 dtype=int
print("0으로 채우기",zero_arr)

# 1로 채워진 배열 생성
one_arr = np.ones((10) , dtype=int )
print(one_arr)

# 문제2 .
# 11부터 22까지의 숫자 12개를 배열에 저장하기
# 위에서 만든 배열을 2차원 배열 3행으로 만들기
#  2차원 배열의 2행 전체의 총합 구하기
#  2차원 배열 전체의 평균 구하기

num = np.arange(11,23)
num2 = num.reshape(3, -1)
print( num2[1].sum() )
print( num2.mean() )
