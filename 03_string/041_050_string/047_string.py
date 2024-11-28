# 047 split 
a047 = "hello world" # 공백을 기준으로 문자열을 나누기
a047_split = a047.split(" ") # split 메서드로 지정한 문자열 즉, 공백(" ")으로 문자를 나눔.
# a047.split(" ") = a047.split() 
# a047.split()에서 ()를 공백 취급하여, 결과값이 똑같음
print(a047_split) 
# 풀이 : split 메서드는 문자열을 분할해줌
# 결과 : ['hello', 'world']