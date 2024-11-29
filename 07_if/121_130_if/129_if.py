# 129 if *답안 확인
users = input("주민등록번호: ")

# 주민등록번호 유효성 체크 공식 
# 1차 계산 : 
# (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 
# 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 
# 2*4 + 1*5)
# = (128 % 11) = 7
num1 =  int(users[0]) * 2 + int(users[1]) * 3 + int(users[2]) * 4 + int(users[3]) * 5 + int(users[4]) * 6 + \
        int(users[5]) * 7 + int(users[7]) * 8 + int(users[8]) * 9 + int(users[9]) * 2 + int(users[10]) * 3 + \
        int(users[11]) * 4 + int(users[12]) * 5
# 2차 계산 : 2차 계산: 11 - 7 = 4
num2 = 11 - (num1 % 11)

# 결과값 문자로 형변환
num3 = str(num2)

# 입력한 데이터가 유효성 공식와 같은지 검사
# True
if users[-1] == num3[-1]:
    print("유효한 주민등록번호 입니다.")
# False
else: 
    print("유효하지 않은 주민등록번호입니다.")

# 결과 : 
# 주민등록번호: 123456-123456   
# 유효하지 않은 주민등록번호입니다.
