# 074 tuple
# t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
# File "<pyshell#46>", line 1, in <module>
# t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
## 에러로 주석처리함.

# 풀이 : tuple은 수정이 불가능한 자료구조임.
# t = (1, 2, 3) 를 t[0] = 'a' 로 수정할려고 시도함. 
# 또한 인덱스 0번째는 0번은 숫자형, 수정할려는 a는 문자열이여서,
# 수정 전에 형변환이 필요함.(물론, 튜플에선 수정자체가 불가능하기 때문에 이럴 일은 없음)

# 결과 :   File "/Users/hwangseoyoung/Documents/aid/python/study/05_tuple/071_080_tuple/074_tuple.py", line 4
#     Traceback (most recent call last):
#                ^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?