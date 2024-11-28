# 028 인덱싱
lang = 'python' 
lang[0] = 'P' 
print(lang) #문자열은 수정 불가능 

# 풀이 : 인덱싱으로 할이 불가능 하기 때문에 P로 수정 시도 시 에러 발생
# 결과물 : 
# raceback (most recent call last):
#   File "/Users/hwangseoyoung/Documents/aid/python/study/python_start/03_string.py", line 56, in <module>
#     lang[0] = 'P'
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment