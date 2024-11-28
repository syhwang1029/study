# 118 if
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
users = input("종목을 입력하세요. ")
if users in warn_investment_list :
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

# 풀이 : users 가 입력한 데이터가 warn_investment_list 리스트 요소에 있으면 
# "투자 경고 종목입니다."이 출력되고(True),
# 요소가 없으면 
# "투자 경고 종목이 아닙니다."가 출력됨(False).

# 결과 :
# 1. 투자 종목인 경우(True)
# 종목을 입력하세요. Microsoft
# 투자 경고 종목입니다.

# 2. 투자 종목이 아닌 경우(False)
# 종목을 입력하세요. 종목
# 투자 경고 종목이 아닙니다.
