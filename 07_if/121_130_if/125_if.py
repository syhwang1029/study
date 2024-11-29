# 125 if
# 입력받은 데이터
users = input("전화번호 입력: ")
# '-'로 전화번호 분할
minus = users.split("-")

# 001인 경우: SKT
if minus == "011":
    a = "SKT"
# 016인 경우: KT
elif minus == "016":
    a = "KT"
# 019인 경우: LGU
elif minus == "019":
    a = "LGU"
# 그외인 경우: 알수없음
else:
    a = "알수없음"

#f-stirng으로 결과 출력
print(f"당신은 {a} 사용자 입니다.")

# 결과: 
# 전화번호 입력: 016-123-4567
# 당신은 KT 사용자 입니다.