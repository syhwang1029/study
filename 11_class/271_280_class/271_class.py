# 271~180 

# 271 class * 답안 확인
<<<<<<< HEAD

# 랜덤 모듈
import random

# 은행 클래스 정의
class Account:
    
    # 메서드 정의
    # 예금주명, 통장잔액
    def __init__(self, name, num):
        self.name = name
        self.num = num
        # 은행명 "SC은행"로 고정
        self.bank = "SC은행" 
        
        # 계좌번호
=======
# 랜덤 모듈
import random

# 은행 클래스
class Account:
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
        # 3자리-2자리-6자리 
=======
        # 계좌 번호  
        # 3자리-2자리-6자리
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
        num1 = str(num1).zfill(3)      
        num2 = str(num2).zfill(2)      
        num3 = str(num3).zfill(6)      

<<<<<<< HEAD
        # 계좌번호 
        self.account_number = num1 + '-' + num2 + '-' + num3  

# 객체 정의
# 메서드 속성 값
hwang = Account("황서영", 100)

# 메서드 출력
print(hwang.name) #예금주명
print(hwang.num) #계좌번호
print(hwang.bank) # 은행명 "SC은행"로 고정 
print(hwang.account_number) #통장잔액

# 결과 : 
# 황서영
# 100
# SC은행
# 537-74-050956
=======
        # 통장잔액
        self.account_number = num1 + '-' + num2 + '-' + num3  

# 셍성자 정의
hwang = Account("황서영", 100)
# 이름, 계좌번호, 은행명, 통장잔액
print(hwang.name)
print(hwang.num)
print(hwang.bank)
print(hwang.account_number)
>>>>>>> e75c8a02c8134ee5910dcd2780327313cab4b5a6
