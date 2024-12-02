# 272 class 클래스 변수

# 랜덤 모듈
import random

<<<<<<< HEAD
# 은행 클래스 정의
class Account:
    # 계좌 갯수 
    # 0 초기화 
    cnt = 0

    # 메서드 정의
    # 예금주명, 통장잔액
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 "SC은행"로 고정
        self.bank = "SC은행" 
        
        # 계좌번호
=======
# 은행 클래스
class Account:
    # 계좌 객체의 개수 
    cnt = 0

    # 이름, 계좌 번호
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 
        self.bank = "SC은행" 
        
        # 계좌 번호
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
        # 랜덤 생성
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

<<<<<<< HEAD
        # 계좌번호  
=======
        # 계좌 번호  
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
        # 3자리-2자리-6자리
        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      

<<<<<<< HEAD
        # 계좌번호
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # 계좌 객체의 갯수 
        Account.cnt += 1


# 예금주 1,2
# 계좌 객체 갯수 확인 1, 2
# 사용자1
hwang = Account("황서영", 100)
print(Account.cnt)
# 사용자2
=======
        # 통장잔액
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # 계좌 객체의 갯수
        Account.cnt += 1


# 셍성자 정의1,2
# 계좌 객체1
hwang = Account("황서영", 100)
print(Account.cnt)
# 계좌 객체2
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
kim = Account("김감자", 200)
print(Account.cnt)

# 결과 :
# 1
# 2