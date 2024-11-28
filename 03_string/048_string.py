# 048 split 
ticker048 = "btc_krw" # btc와 krw로 나누기
ticker048_split = ticker048.split("_") # split 메서드로 지정한 언더바(_)를 기준으로 문자를 나눔.
print(ticker048_split)
# 풀이 : split 메서드는 지정한 문자열을 기준으로 문자를 분할해줌
# 결과 : ['btc', 'krw']