# 274 class 출금 메서드
# *답안 확인
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
    # 생성된 계좌의 갯수 
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)
    # 입금 메서드 
    def deposit(self, amount):
        if amount >= 1:
            self.num += amount
    
    # 출금 메서드 추가
    def withdraw(self, amount):
        # 통장잔액보다 적은 경우만 출금가능
        if self.num > amount:
            # 통장잔액에서 차감
            self.num -= amount
            
    
# 사용자 1
# 출금 확인
kim = Account("김감자", 200) # 기존 통장잔액
kim.deposit(100) # 입금 금액
kim.withdraw(90) # 출금 금액 
print('사용자1의 통장잔액 : ', kim.num) # 기존 통장잔고+입금 금액 = 현재 통장잔액
# 결과 :
# 사용자1의 통장잔액 :  210