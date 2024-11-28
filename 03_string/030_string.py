# 030 replace *답안확인
string30 = 'abcd'
string30_1 = string30.replace('b', 'B') #소문자 b를 대문자 B로 변경
print(string30_1) # 'abcd' -> 'aBcd'로 예상 
# 풀이 : replace 함수를 활용하여 aBcd로 예상됨(오답)
# 정답지 : 문자열은 변경할 수 없기 때문에 변형없이 그대로 출력됨
#  replace 메서드는 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줌
# 결과물 : abcd

## aBcd로 변경하고 싶은 경우
# string30 = 'abcd'
# string30_1 = string30.replace('b', 'B') #새로운 변수 string30_1에 변수값이 할당되기 때문에, 변경이 가능함.
# print(string30_1) 
