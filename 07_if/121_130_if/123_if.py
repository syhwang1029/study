# 123 if * 답안 확인
 
# 각종 나라별 돈 딕셔너리
money = {"달러":1167, "엔":1.096, "유료":1268, "위안":171}

# value 값만 생성
# money_values = money.values()
# money_values = float(money_values)

# 입력받은 데이터
users = input("입력: ")
num, money  = users.split()

# 숫자형 변환
#user = float(users)

# 입력받은 데이터 * 돈  
#won = money_values * user 

#결과
print(float(num) * money, "원")
