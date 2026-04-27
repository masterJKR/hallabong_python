#function1.py

#  제어자 반환타입 메서드이름( 매개변수 ) 

# 파이썬 함수 -  def 함수이름(매개변수):

def hi():
    print("안녕")


# 함수 실행 - 호출
# 함수이름() - () 소괄호에 매개변수가 있다면  넣어주기
hi()


def intro(name : str):
    print( name, "님 로그인 하셨습니다.")


name = "김유신"
if type(name) == str:  # isinstance( name , str)
    intro(name)


intro("하늘소")
intro("감기약")
intro(1000)


def dataInput(a,b,c):
    print( a + b + c)

dataInput(1,20,30)

# 함수를 만들때(정의)  어떤 기능을 가진 함수를 만들것인가  
#  해당 기능이 작동 되기 위해서  필요한것이 무엇인가
#  필요한것들이  함수 안에서 만들수 있는것인가  아니면  외부에서 받아야 하는것인가

# 함수의 반환값  return - 함수가 호출된 위치로 값을 돌려보내는 작업, 그리고 함수의 종료

def add( num1 , num2 ):
    return "계산 결과 " , num1 + num2


comment , res = add( 10, 20 )
print(comment , res)


# 변수의 범위  -  지역변수 ,전역변수 

number = 1000



def totalPrice( price ):
    total = 0
    for money in price:
        total += money
    global number 
    number = total  # 전역변수의 수정은  안된다.  global을 붙여줘야 수정가능



totalPrice( [ 1,2,3,4,5] )
print( number )


# 문제1.  간단한 함수만들기  
#   사각형의  너비와 높이를  받아서  넓이를 출력하는 함수를 만들어  호출해보세요
#  함수에서 넓이 구하는계산식 있어야 하고 출력도 있어야 한다.

def square(width, height):
    res = width* height
    print("넓이는 : ", res)

square(20 , 5)


#문제 2.  아래 코드를 보고  함수를 만드세요
# 로그인 체크 함수 만들기

def login_check(id, pw):
    if id=="admin" and pw=="1234":
        return True
    else: return False
    


id=input("아이디를 입력하세요")
pw=input("비밀번호를 입력하세요")

if login_check(id,pw):   # 여기 부분 을 함수로 처리 될수 있게
    print("로그인 성고 하여습니다.")
else:
    print("아이디 또는 비밀번호를 잘못 입력 했습니다.")


#문제3 .  상품의 재고를 확인하여  재고 충분, 재고 부족, 품절  이라고 출력 할수 있는 함수만들기
#  재고 부족 기준은  현재 재고량이 8이하인 경우

item_stock = 12

if item_stock > 8:
    print(" 재고 충분 ")
elif item_stock > 0 :
    print("재고 부족")
else :
    print("품절")

# 위 코드를  print( 함수 호출 )  이렇게 실행 하면 동작하수 있게 함수 만드세요 

def stock_check( stock ):
    if stock > 8:
        return "재고 충분"
    elif stock >0 :
        return "재고 부족"
    else:
        return "품절"
    
print( stock_check(item_stock) )


# 문제 4.   회원가입을 한다.  아이디 중복체크 함수를 만드세요

id_list=["kim", "lee","sky", "gold", "war123", "qwer12", "eeeel4" ]

# id_list는  현재 가입된 회원들의 아이디만 저장된 리스트이다. 
# 아이디 중복체크 함수를 통해  사용가능, 불가능을 출력하세요

def id_check( id ):
    global id_list
    if id in id_list:
        return "사용불가능"
    else:
        return "사용가능"
    
print( id_check("park")  )