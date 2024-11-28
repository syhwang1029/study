# 035 % formatting 메서드 중 %s, %d
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1)) 
print("이름 : %s 나이 : %d" % (name2, age2))
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13 이 출력되어야 함
# 풀이 : % formatting 중 %s는 문자열, %d는 숫자형을 나타냄
# 결과물 : 
# 이름 : 김민수 나이 : 10
# 이름 : 이철희 나이 : 13