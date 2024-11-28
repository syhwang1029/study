# 090 dictionary  
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

## 에러 발생으로 주석처리

# 풀이 : 에러 원인은 '누가바' 라는 key에 value를 할당하지 않았기 때문임.
# 또한 '누가바' 라는 key 자체가 존재하지 않기에, 데이터 재할당도 불가능함.

# 결과 :   File "/Users/hwangseoyoung/Documents/aid/python/study/06_dictionary/081_090_dictionary/090_dictionary.py", line 8
#     KeyError: '누가바
#               ^
# SyntaxError: unterminated string literal (detected at line 8)