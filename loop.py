# loop.py

print("숫자 : 1")
print("숫자 : 2")
print("숫자 : 3")
print("숫자 : 4")
print("숫자 : 5")

# 5번 반복하는 반복문
for i in range(5,1,-1):
    print("숫자 : " + str(i) )

print("=====================")

for ch in "hello":
    print(ch)

for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"]:
    if name.startswith("이") :
        print(name)

#문제1. 1부터 10까지의 총합을 구하세요. 반복문을 사용해서

sum = 0
for i in range(1,11):
    sum = sum + i

print( "총합 : " +str(sum) )

#문제 2. ["15,000",  "13,000", "8,700",  "9,000", "25,000"]
# 배열에  출금 금액들이 저장되어있다.  
# 만원 이상 금액들에 대해  출력하세요

money = ["15,000",  "13,000", "8,700",  "9,000", "25,000"]
for m in money:
    temp =int(m.replace("," , ""))
    if temp >= 10000 :
        print(m)

for i in range( len(money) ):
    print("금액 : ", i , money[i] )

for i, v in enumerate(money):
    print( i ,  v  )


#문제 3.    [89 , 56 , 78, 92, 61, 96, 83, 74]
# 203호 학생들의 성적이다.  성적의 총합과 평균을 출력하세요
# 80점 이상인 학생들의 위치(인덱스)도 출력하세요

student_score = [89 , 56 , 78, 92, 61, 96, 83, 74]
total = 0  # 총점 구하기 변수
for i,v in enumerate(student_score):
    total = total+v  # total += v
    if v>=80:
        print("80점이상 학생 위치 : ", i )

print("총점 : ",total)
print("평균 : " , total/len(student_score) )



# 반복문  while

# while 조건:
#     실행코드

# while문은 조건식이 참인경우에 동작 하기떄문에 
#  쉽게 무한루프에 들어갈수 있다.  
#  하여  while문 사용시  중단시킬수 있는  break를 같이 사용하는게 좋다.

num = 5
while num > 2:
    print("2보다 크다")
    break

while True:
    num+=1 # num = num +1
    if num == 7: continue  # 건너뛰기
    print( num )
    if num == 10: break

print("=============")
# while True:
#     cmd = input("명령어 입력 : " ).strip().lower()
#     if cmd == "history":
#         print("모든 기록 출력")
#     elif cmd == "mkdir":
#         print("새로운 폴더 만들기")
#     elif cmd == "remove":
#         print("파일 삭제")
#     elif cmd == "exit":
#         print("종료")
#         break
#     else:
#         print("존재하지 않는 명령어 입니다.")

# 파이썬 랜덤 사용
import random

num = random.randint(1,10)
print( num )

# 동전 앞면 뒷면  맞추기  게임 만들기

coin = random.randint(1,2)
user = int(input("1.앞면, 2.뒷면 : " ) )
if coin == user:
    print("정답!")
else:
    print("땡!!")

n = random.randrange(1,10)  # 1~9

def compare(a,b):
    if a>b: return 1
    elif a<b : return -1
    else: return 0



# 가위바위보 게임  5판 진행.  
#  5번째 게임이 끝나면  몇승 몇패 몇무인지 출력

# game = ["가위","바위","보"]

# win = lose = draw = 0
# for i in range(5):
#     com = random.choice(game)
#     user = input("가위 바위 보 : ").strip()

#     print("컴퓨터 : ",com , " 나 : " ,user)
#     # 승 패 무 판단
#     #game.index("가위")
#     # 사전적 순서 비교  방법 은 비교연산자 
#     cidx = game.index(com)
#     uidx = game.index(user)

#     comp = cidx - uidx  # 유저와 컴의 가위바위 보값 비교
#     # 가위-0, 바위-1, 보-2 ->  유저가 0 컴이 1이라면 컴의승 
#     # 즉 comp에 1이 있다면 컴의 승

#     if com == user:
#         print("비김")
#         draw+=1
#     elif comp== -1 or comp==2:
#         print("나의 승")
#         win+=1
#     else:
#         print("나의 패")
#         lose+=1
# print("승 : ",win,"  패 : ",lose," 무 : ",draw)
a=["돈가스","라면","짬뽕","짜장면","볶음밥","순대국밥"]
random.shuffle(a)
print(a)

b = random.sample(range(1,46), 6)
print(b)