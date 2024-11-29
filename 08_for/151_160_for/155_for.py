# 155 for

# 알파벳 리스트
eng = ["A", "b", "c", "D"]
# uppers 변수에 리스트 할당
for uppers in eng:
    # 대문자 판별 후 대문자인 경우만 출력
    if uppers.isupper() == True:
        # 대문자만 출력
        print(uppers)
        
# 결과 : 
# A
# D