# 113 if *답안 확인
users = input("숫자를 입력하세요: ") # 짝/홀 판단
if int(users) % 2 == 0: # int로 형변환 후 계산
    print("짝수")
else:
    print("홀수") 

# 풀이 : input() 함수로 데이터를 입력받음.
# int() 함수로 입력받은 데이터로 숫자로 형변환되며, 
# % 산술연산자(나머지 계산)로 2로 나누기가 되는 경우는 짝수,
# 나누기가 되지 않는 경우는 홀수임.

# 이때 0는 정수로 계산하기 위해서임.

# 결과 : 
# 숫자를 입력하세요: 10
# 짝수