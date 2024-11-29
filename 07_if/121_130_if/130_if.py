# 130 if
import requests  
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동 : 시가 - 최저  
fluctuation = float(btc['opening_price']) - float(btc['min_price']) 
opne = float[btc['opening_price']]# 시가 
max = float[btc['max_price']] # 최고가

# 시가 + 변동 = n 
# n > 최고가 
# n 보다 큰 경우 : 상승장
if (open+fluctuation) > max:
    print("상승장")

# n 보다 작은 경우 : 하락장
else:
    print("하락장")


# 결과 : 
