# 187 for

# 호수 리스트
apart = [ [101, 102], [201, 202], [301, 302] ]

# 리스트를 row 변수에 저장 
# 반댓 방향으로 지정
for row in apart[::-1]:
    # row를 col 변수에 저장
    # 반댓 방향으로 지정
    for col in row[::-1]:
            # 결과값
            print(col, "호")

# 결과 :
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호