# 279 class 
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
            
            # 입금횟수 5회마다 1%의 이자 지급
            self.cnt += 1
            # 입금 숫자
            if self.cnt % 5 == 0 :
                self.num = (self.num *1.01) 
    
    # 출금 메서드 추가
    def withdraw(self, amount):
        # 통장잔액보다 적은 경우만 출금가능
        if self.num > amount:
            # 통장잔액에서 차감
            self.num -= amount
            
    # Account 인스턴스 정보 저장 메서드 추가
    # 은행명, 예금주명, 계좌번호, 통장잔액
    def display_info(self):
        print('은행명: ', self.bank)
        print('예금주명: ', self.name)        
        print('계좌번호: ', self. account_number)
        print("통장잔액: ", f"{self.num:,}", "원")
# 리스트 초기화 저장
ls = []
# 사용자 1,2,3 정보
p = Account('파이썬', 1000)
k = Account('김선아', 2000)
m = Account('문혜림', 10000000)
ls.append(p)
ls.append(k)
ls.append(m)
for bn in ls:
    if bn.num >= 1000000:
        bn.display_info()
    
print(p.display_info())
print(k.display_info())
print(m.display_info())