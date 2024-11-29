# 122 if
# 입력받은 데이터 
# 조건은 숫자 비교이므로 int로 형변환
score = int(input("score: "))

# 81점~100점 인 경우
if 81<= score <= 100:
   print("grade is A")

# 61점~80점 인 경우
elif 61<= score <= 80:
    print("grade is B")

# 41점~60점 인 경우
elif 41<= score <= 60:
    print("grade is C")  

# 21점~40점 인 경우
elif 21<= score <= 40:
    print("grade is D")      

# 그 이하인 경우
else:
    print("grade is E")

# 결과 :
# 1. 21점 이하인 경우
# score: 0 
# grade is E

# 2. 41점~60점 인 경우
# score: 58
# grade is C