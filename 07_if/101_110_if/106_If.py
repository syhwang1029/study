# 106 if
# print(3 => 4)
## 에러 발생으로 주석처리함.

# 풀이 : => 은 올바른 형식이지 않아 에러 발생함.
# 올바른 형식은 >= 임.

# 결과 :     print(3 => 4)
#           ^^^
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?


print(3 >= 4) # 올바른 형식
# 풀이 4는 3보다 작거나 같지 않기 때문에 False임.
# 결과 : False
