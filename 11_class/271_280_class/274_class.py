<<<<<<< HEAD
# 274 class 입금 메서드
#* 답안 확인
=======
# 274 class  입금 메서드
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6

# 랜덤 모듈
import random

# 은행 클래스
class Account:
    # 계좌 객체의 개수 
    cnt = 0

<<<<<<< HEAD
    # 메서드 정의
    # 예금주명, 통장잔액
=======
    # 이름, 계좌 번호
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 
        self.bank = "SC은행" 
<<<<<<< HEAD

        
        # 계좌번호
=======
        
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
=======
        # 통장잔액
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
        self.account_number = num1 + '-' + num2 + '-' + num3  

        # 계좌 객체의 갯수
        Account.cnt += 1

<<<<<<< HEAD
    # 계좌의 갯수 메서드  
=======
    # 클래스 메서드  
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
    @classmethod
    def get_account_num(clsm):
            print(clsm.cnt)

<<<<<<< HEAD
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
=======
    # 입금 메서드
    def deposit(self, deposit):
        if deposit >= 1:
            self.num += deposit


# 셍성자 정의1,2
# 계좌 객체1, 2
# 입금 
hwang = Account("황서영", 100)
hwang.deposit(1000)
kim = Account("김감자", 200)
kim.deposit(2000)
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
