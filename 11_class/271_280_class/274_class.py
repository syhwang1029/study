# 274 class 입금 메서드
#* 답안 확인

# 랜덤 모듈
import random

# 은행 클래스
class Account:
    # 계좌 객체의 개수 
    cnt = 0

    # 메서드 정의
    # 예금주명, 통장잔액
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 
        self.bank = "SC은행" 

        
        # 계좌번호
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

    # 계좌의 갯수 메서드  
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)

    # 입금 메서드 추가
    def deposit(self, amount):
        # 1원 이상만 입금 가능
        if amount >= 1:
            #통장잔액에 증감
            self.num += amount


# 사용자 1,2
# 입금 확인
hwang = Account("황서영", 100) # 기존 통장잔액
hwang.deposit(1000) # 입금액
# 기존 통장잔액 + 입금액 = 현재 통장잔액
print('사용자1 통장잔액 : ', hwang.num)
kim = Account("김감자", 200)
kim.deposit(200)
print('사용자2 통장잔액 : ', kim.num)

# 결과 :
# 사용자1 통장잔액 :  1100 
# 100+1000=11000
# 사용자2 통장잔액 :  400
# 200+200=400