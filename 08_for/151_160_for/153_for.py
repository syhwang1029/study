# 153 for *답안 확인

# 숫자 리스트
numls =  [13, 21, 12, 14, 30, 18]

# drainage 변수에 리스트 할당
for drainage in numls:
    # 20보다 작고, 3의 배수
    if drainage<20 and drainage%3 == 0:
        print(drainage)

# 결과 :
# 12
# 18