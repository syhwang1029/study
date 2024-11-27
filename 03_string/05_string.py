# 3.파이썬 문자열 
# 041~050

# 041 upper
ticker041 = "btc_krw"
ticker041_upper = ticker041.upper() # upper 메서드로 btc_krw을 대문자로 변환 함
print(ticker041_upper)
# 풀이 : upper 메서드는 모든 글자를 대문자로 변환해줌 
# 결과물 : BTC_KRW

# 042 lower 
ticker042 = "BTC_KRW"
ticker042_lower = ticker042.lower() # lower 메서드로 BTC_KRW를 대문자로 변환함
print(ticker042_lower) 
# 풀이 : lower 메서드는 모든 글자를 소문자로 변환해줌
# 결과 : btc_krw

# 043 capitalize 
ticker043 = 'hello'
ticker043_capitalize = ticker043.capitalize() # capitalize 메서드로 첫글자 H만 대문자로 변환함
print(ticker043_capitalize)
# 풀이 : capitalize 메서드는 첫글자만 대문자로 변환해줌
# 결과 : Hello

# 044 endswith
file_name044 = "보고서.xlsx" # 'xlsx'로 끝나는지 확인
file_name044_endswith  = file_name044.endswith("xlsx") # endswith 메서드로 xlsx로 끝나는지 판단함
print(file_name044_endswith)
# 풀이 : endswith 메서드는 지정한 문자열로 끝나는지 판단한 후 bool로 반환함
# 참인 경우는 True이고, 거짓인 경우는 False임
# xlsx로 끝나기 때문에 True로 반환됨
# 결과 : True

# 045 endswith
file_name045 = "보고서.xlsx" # 'xlsx' 또는 'xls'로 끝나는지 확인
file_name045_endswith = file_name045.endswith("xlsx" and "xls") 
# endswith 메서드로 'xlsx' 또는(and) 'xls'로 끝나는지 확인함
print(file_name045_endswith) 
# 풀이 : endswith 메서드로 변수는 xlsx로 끝나기 때문에, False로 반환됨
# 결과 : False

# 046 startswith
file_name046 = "2020_보고서.xlsx" # '2020'로 시작하는지 확인
file_name046_startswith = file_name046.startswith("2020") 
# startswith 메서드로 문자열 '2020'로 시작하는지 판단함 
print(file_name046_startswith)
# 풀이 : startswith 메서드는 지정한 문자열로 시작하지 판단한 후 bool로 반환함
# 문자열 2020으로 시작되기 때문에 True로 반환됨
# 결과 : True 

# 047 split 
a047 = "hello world" # 공백을 기준으로 문자열을 나누기
a047_split = a047.split(" ") # split 메서드로 지정한 문자열 즉, 공백(" ")으로 문자를 나눔.
# a047.split(" ") = a047.split() 
# a047.split()에서 ()를 공백 취급하여, 결과값이 똑같음
print(a047_split) 
# 풀이 : split 메서드는 문자열을 분할해줌
# 결과 : ['hello', 'world']

# 048 split 
ticker048 = "btc_krw" # btc와 krw로 나누기
ticker048_split = ticker048.split("_") # split 메서드로 지정한 언더바(_)를 기준으로 문자를 나눔.
print(ticker048_split)
# 풀이 : split 메서드는 지정한 문자열을 기준으로 문자를 분할해줌
# 결과 : ['btc', 'krw']

# 049 split 
date049 = "2020-05-01" # 연도, 월, 일로 나누기
date04_split = date049.split("-") 
print(date04_split) # split 메서드로 붙임표(-)를 지정하여 이를 기준으로 문자를 나눔.
# 풀이 : split 메서드는 문자열을 지정하여 이를 기준으로 분열함.
# 결과 : ['2020', '05', '01']

#050 rstrip 
data050 = "039490     " # 오른쪽 공백 제거
data050_rstrip = data050.rsplit() # rsplit 메서드로 오른쪽 공백을 제거함
print(data050_rstrip)
# 풀이 : rstlit 메서드는 오른쪽 공백()을 제거해줌
# 결과 : ['039490']