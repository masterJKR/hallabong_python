# numpy_test.py

import numpy as np
arr = np.array([10,20,30,40,50]) # numpy 배열생성
print(arr)
print( type(arr) )
print( arr[0] )
print( arr[-2] )
arr[0] = 100
print( arr[0] )
print( [1,2,3] + [4,5,6] )

print( np.array([1,2,3]) + np.array([4,5,6]) )

print( arr + 10 )

print( len(arr) )
print( arr.shape ) # (5,) : 데이터 5개 1차원 배열
print( arr.dtype )
#  int32 ,int 64  정수타입
# float32 , float64 실수
#  uint8  이미지
# bool  논리 타입

score = np.array( [88, 94, 53, 67, 72] )
print("점수 : " , score)

print( "평균 : " , score.mean() )

print( "총합 : " ,score.sum() )

print(" 최대값 : " , score.max() )
print("최소값 : ",score.min() )


# 이미지 또는 영상  shape 결과 - (720, 1280, 3)

'''
numpy는  파이썬에서 숫자 계산을 빠르게 하기 위한 라이브러리이다.
1+2+3
[1,2,3]  +  [4,5,6]

'''