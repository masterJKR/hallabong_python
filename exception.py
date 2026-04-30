#  exception.py

print("오류??")

print( 2 + 2 )

try:
    print(  10 / 0 )
except:
    print("오류인가?")


try:
    num = int(input("숫자입력 : " ))
    print(num)
except Exception as e :
    print(e)


# try:
#     오류가 예상되거나 사용자와 밀접한 코드
# except FileNotFoundError:

# except KeyError:


# try:
#     f = open("a.txt","r")
# except FileNotFoundError:
#     print("존재 하지 않는 파일입니다.")
# finally:
#     f.close()
#     print("오류가 있어도 없어도 실행")

try:
    with open("a.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("존재하지 않는 파일입니다.")
else:
    print("오류가 없을때만 실행 ")

# 숫자입력을  잘 할때까지  계속 입력 받기 


def check_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 한다")
    

while True:
    try:
        num = int(input("나이 : "))
        check_age(num)
        break
    except ValueError as e:
        print(e)
    except:
        print("다시 입력하세요")


'''
    ValueError  -  값이 잘못된경우
    TypeError - 타입이 맞지 않은 경우
    ZeroDivisionError  - 0으로 나눔
    IndexError  - 인덱스 범위 초과 
    KeyError  -  딕셔너리 키 없는경우
    NameError  -  변수없는 경우 
    AttributeError - 속성/메서드 없는경우
    FileNotFoundError - 파일없는경우

'''