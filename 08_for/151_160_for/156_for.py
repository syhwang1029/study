# 156 for

# 알파벳 리스트 
eng = ["A", "b", "c", "D"] 
# lowers 변수에 리스트 할당
for lowers in eng:
    # 소문자 판별 후 소문자인 경우만 출력
    if lowers.islower() == True:
        # 소문자만 출력
        print(lowers)

# 결과 :
# b
# c