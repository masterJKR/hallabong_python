from member_service import login

print( login.login_process("gold", "123456"))


'''
auth 폴더 생성
   -  valid.py
   -  sign_in.py

   valid.py - 아이디 길이 체크 함수, 비밀번호 최소 길이 체크 하는 함수
   sign_in.py  -  valid.py 사용 ,  db.py 사용,  로그인처리 

   아이디 길이는 4 ~ 12자  ,  비밀번호는 최소 6 자

   vaild.py의  함수들 을 통과해야  db.py를 통해 아이디 ,비밀번호 가져올수 있다.
'''