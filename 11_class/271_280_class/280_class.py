# 280 class 입출금 내역
# *답안 확인 
import random

# Account 클래스 정의
class Account:
  
    # 계좌 갯수
    account_count = 0

    # 예금주명, 통장잔액
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = [] #입금 내역
        self.withdraw_log = [] #출금 내역

        self.name = name
        self.balance = balance
        self.bank = "SC은행" #은행명은 고정

        # 계좌번호
        # 랜덤 생성
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        
        # 3자리-2자리-6자리
        num1 = str(num1).zfill(3)  
        num2 = str(num2).zfill(2)  
        num3 = str(num3).zfill(6)  
        self.account_number = num1 + '-' + num2 + '-' + num3 
        Account.account_count += 1
    
     # 생성된 계좌의 갯수 
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  
     # 입금 메서드 
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            # 입금횟수 5회마다 1%의 이자 지급
            self.deposit_count += 1
            # 입금 숫자
            if self.deposit_count % 5 == 0:         
                # 이자 지금
                self.balance = (self.account_count * 1.01)

    # 출금 메서드 추가
    def withdraw(self, amount):
        # 통장잔액보다 적은 경우만 출금가능
        if self.account_count > amount:
            self.withdraw_log.append(amount)
            # 통장잔액에서 차감
            self.balance -= amount

    # Account 인스턴스 정보 저장 메서드 추가
    # 은행명, 예금주명, 계좌번호, 통장잔액
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    # 입금
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
    # 출근
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

# 사용자 정보
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

# 결과 :
# 100
# 200
# 300
# 100
# 200

