# 120 if
# 딕셔너리
fruit = {"봄" : "딸기", 
         "여름" : "토마토", 
         "가을" : "사과"}
# value 값만 생성
fruit = fruit.values()
# 입력받은 데이터
users = input("좋아하는 과일은?")
if users in fruit:# True인 경우
    print("정답입니다.") 

else: #False인 경우
    print("오답입니다.") 

# 결과 
# 1. True인 경우
# 좋아하는 과일은?딸기 
# 정답입니다.

# 2. False인 경우
# 좋아하는 과일은?한 참외
# 오답입니다.