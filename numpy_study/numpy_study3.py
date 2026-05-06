# numpy_study3.py

import numpy as np

# 배열에서  원하는 위치 데이터 가져오기

arr = np.random.randint(0, 50 ,  12)
print(arr)

#슬라이싱
print( arr[3:8] )
print( arr[:4])  # :4 -> 0번인덱스부터 3번까지
                 #  2:  ->  2번인덱스부터  끝까지
print( arr[::2] )  # ::2  -> 2칸씩
print( arr[::-1] )  #역방향으로 출력


arr2 = np.random.randint(0,50 ,(3,4) )
print(arr2)
print( arr2[1] )
print( arr2[: ,2])
print( arr2[0:1, 1:3])


#fancy indexing :  원하는 위치만 고르기
print( arr[[0,4,7]])  #  [ [ 인덱스, 인덱스  ] ] 원하는 인덱스번호 넣기

print( arr2[[0,2]]  )  # 2차원배열에서는  행을 선택
print( arr2[ [0,2] , [1,3] ])  #  0,1 (arr[0][1])   과   2,3 (arr[2][3])


# boolean indexing
print( arr > 30  )
print( arr[ arr>30 ]  )  #  조건식에 맞는 데이터만 뽑아 내기
print( arr[arr % 2 == 1])


print( arr2[ arr2 > 15 ] )

# 학생 5명의  6과목 성적을  배열로 저장하세요 ( 성적은 50~100 사이 임의값)
# 학생 5명 성적이 저장된 배열에서  성적이 80점이상만 출력하시오

scores = np.random.randint(50,100,(5,6))
print(scores[scores>=80])

pos = np.argwhere( scores>=80)
print(pos)