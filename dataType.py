#dataType.py
# 리스트,  튜플
#리스트 - 여러 데이터를 저장 관리 하기 위한 파이선 자료구조이다.  
#튜플도 리스트와 같은데  차이점은   리스트는 수정이 가능하지만
#  튜플은 수정이 불가능하다. 

# 리스트 - 순서 유지, 인덱스를통해 접근,  추가,수정,삭제가능
#   다른 자료형도  저장가능  
number = [ 10, 20, 30, 40, 50 ]
empty = [] 
name = list()

print( number[0]  )
print( number[-2] )

# 리스트 자르기
num = number[2:4]
print( num )
num2 = number[:3]
print( num2 )
num3 = number[2:]
print( num3 )

# 리스트 수정
number[2] = 100
print( number )

#리스트 추가
number.append(60)  # 리스트의 마지막에 추가
print(number)

number.insert(2,500)  # 리스트에 원하는 위치에 추가(인덱스, 값)
print( number )
a=10
#리스트 값 삭제
number.remove(100)  # 리스트에서 삭제 할  데이터 입력
print( number )
number.pop(1)  # 리스트에서 삭제할 데이터의 인덱스 입력
print( number )
del number[2]  # 인덱스로 삭제
print( number )

#리스트 크기 (길이)
print( len(number) )

for num in number:
    print( num )

for i , num in enumerate(number):
    print(i, num )

# 리스트 검색
print(  40 in number )  #  값의 존재여부 True, False
print(  number.index(50) ) # 인덱스 찾기 - 없으면 오류
# index를 통해 인덱스를 찾기 전에 in으로 존재여부 확인 먼저 하기

#리스트 정렬 
number.sort()  # 기본 정렬은 오름차순이다.
print(number)
number.sort(reverse=True)
print( number )

#리스트 는  일반적으로 많이 사용되는 자료구조이다.  
# 자바에서 List (ArrayList)를 많이 사용 된다면  파이썬은 리스트이다.
# 여러데이터를 저장할수 있고 ,수정, 추가 가능하고  반복문 사용 쉽고
# 정렬, 검색도 되고  그래서 사용하기 좋은 녀석이다.!


#리스트 문제 풀기!!!!!
# 문제1.  5명의 이름이 저장되어 있는 리스트 만들기
#   5명의 이름  출력하는 반복문 만들기

names = ["이순신","강감찬","이성계","문익점","한석봉"]
print( type(names))
for name in names:
    print(name)

# 문제2.  정도전  이름을 추가하고 출력하세요 
names.append("정도전") # 원하는 위치 추가는 insert
print( names )

# 문제 3.  리스트에  김유신 이 있는지 확인하는 코드 작성하기 
if "김유신" in names:
    print("등록된 이름이다")
else:
    print("등록되지 않은 이름이다.")

#문제 4.  이름 리스트에  내림차순으로 정렬 하여 출력하세요
names.sort(reverse=True)
print( names )

# 문제 5.   과일의 이름이 두글자인 과일만 출력하세요
# 힌트 : len
fruits = ["사과","바나나","파인애플","딸기","오렌지","포도","배"] 

for f in fruits:
    if len(f)==2:
        print(f)

fruits.sort(key=len)
print(fruits)

#문제  6. 과일 검색 프로그램 만들기
#  과일이름 키보드를 통해 입력받는다.
#  입력한 과일이  리스트에 있다면  판매중,  없다면 품절 이라고 출력

# fname = input("과일 입력 : ").strip()
# if fname in fruits:
#     print("판매중")
# else:
#     print("품절")
# for fruit in fruits:
#     if fname == fruit:
#         print("판매중")
#     else:
#         print("품절")

# 문제 7.   구매 할 과일 을 입력 하면  총 지불금액 얼마인지 출력
#  단, 과일은 1개를 구매할수도 있고 여러개 구매할수도 있어야 한다.

# fruits.sort() # 딸기, 바나나,배,사과,오렌지,파이애플,포도
# price = [5000, 8000, 12000,9500, 15500, 20400, 9000]

# fname = input("구매할 과일 입력 : ").split()

# total = 0

# for f in fname:
#     if f in fruits:
#         idx = fruits.index(f)
#         total += price[idx]
# print("총 금액 : ", total)


# 튜플 -  리스트처럼 여러 데이터를 저장 할수 있는 자료형이다. 
#    저장한  데이터를 수정 할 수 없다.
#  데이터를 보호 하기 위한 목적 
#  속도와 메모리 효율 성  
#  딕셔너리의  키로 사용 
# 여러개의 값을 반환(return) 시킬때

# 튜플 만들기  
number = (10,20,30,40)  # 작은괄호 -튜플 , 대괄호 - 리스트
print(number)
print( type( (1,2,3,4) ))
print( type( (10,)  ))

print( number[1] ) # 인덱스 0 부터 시작 

#  number[0] = 100  값 수정 은 오류

# 튜플 슬라이싱( 자르기 )
print( number[1:3] )

# 튜플 검색
print(  10 in number)
print( number.index(20)  )

#  리스트와 다른점 
# 수정 불가 , 추가 불가, 삭제 불가
# number.append(200) 오류
# number.remove(20) 오류 
# number.pop(20) 오류
# del number[2]

print(  number.count(20)  )  # 특정값 갯수 구하기

data = 10,20,30,40,50  # 패킹 - 여러값을 하나로 묶기
print( type(data)  )

a,b,c,d,e = data   # 언패킹 -  묶여있는 값을 여러개로 나누기
print( a, b, c, d, e)

red = 20
blue = 10

red , blue = blue,red
print( red, blue )


# 함수 반환 여러개 
def get():
    return 10,20,30,40


# 리스트 <--> 튜플
info = ("다음주","금요일","빨간날","그래서","우리는","5월6일에","봐요")
#info[0]="이번주"  오류

info_list = list(info)  # 튜플 -> 리스트로 변환
info_list[0]="이번주"

info = tuple(info_list)  #  리스트 -> 튜플 변환
print( info )