# 273 class 클래스 변수 출력
# * 답안 확인

# 랜덤 모듈
import random

# 은행 클래스
class Account:
    # 계좌 객체의 개수 
    cnt = 0

    # 이름, 통장잔액
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 
        self.bank = "SC은행" 
        
        # 계좌 번호
        # 랜덤 생성
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        # 계좌번호  
        # 3자리-2자리-6자리
        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      

        # 계좌번호
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # 계좌 객체의 갯수
        Account.cnt += 1

    # 생성된 계좌의 갯수 출력 추가
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)


# 사용자 1,2,3
# 계좌 객체1,2,3
# 사용자1
hwang = Account("황서영", 100)
hwang.get_account_num()
# 사용자2
kim = Account("김감자", 200)
kim.get_account_num()
# 사용자3
pack = Account("박민주", 300)
pack.get_account_num()

# 결과 :
# 1
# 2
# 3