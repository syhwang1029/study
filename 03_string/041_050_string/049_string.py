# 049 split 
date049 = "2020-05-01" # 연도, 월, 일로 나누기
date04_split = date049.split("-") 
print(date04_split) # split 메서드로 붙임표(-)를 지정하여 이를 기준으로 문자를 나눔.
# 풀이 : split 메서드는 문자열을 지정하여 이를 기준으로 분열함.
# 결과 : ['2020', '05', '01']