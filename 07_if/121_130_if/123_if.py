# 123 if * 답안 확인
 
# 각종 나라별 돈 딕셔너리


money = {
        '달러':1167, 
        '엔':1.096,
        '유료':1268,
        '위안':171
         }
# value 값만 생성
money_values = money.values()

# 입력받은 데이터
users = input("입력: ")
# 숫자형 변환
user = float(users)

# 곱하기 
won = user * money_values
print(won)
