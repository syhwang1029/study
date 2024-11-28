# 115 if
users = input("값을 입력하세요: ")
users = int(users) - 20

#범위 0~255
if users < 0: # 입력받은 데이터가 0보다 작은 경우 
    print(0) # 0 출력

elif users > 255: # 입력받은 데이터가 255보다 큰 경우
    print(255) # 255 출력

else: # 그외의 경우
    print(users) # 입력한 데이터 그대로 출력

# 풀이 : input() 함수에서 데이터를 입력받음.
# int() 함수로 형변환 후 20을 뺌. -> 비교할 데이터
# 0보다 작은 경우, 0 반환.
# 255보다 큰 경우, 255 반환.
# 이는 0~255로 범위로 조건으로 지정함.
# 그외는 입력한 데이터 그대로 반환(출력).

# 결과 : 
# 1. 입력값 : 0
# 값을 입력하세요: 0
# 0
# 2. 입력값 : 300 
# 값을 입력하세요: 300
# 255
# 3. 입력값 : 80
# 값을 입력하세요: 80
# 60