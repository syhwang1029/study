# 119 if 
# 딕셔너리
fruit = {"봄" : "딸기", 
         "여름" : "토마토", 
         "가을" : "사과"}
# key 값만 생성
fruit = fruit.keys()
# 입력받은 데이터
users = input("내가 좋아하는 계절은?")

if users in fruit: # True인 경우
    print("정답 입니다.")

else: #False인 경우
    print("오답 입니다.")
# 결과 : 
#1. True인 경우
# 내가 좋아하는 계절은? 봄 //key 값을 입력함
# 정답 입니다.

#2. False인 경우
# 내가 좋아하는 계절은? 딸기 //value 값을 입력함
# 오답 입니다.
