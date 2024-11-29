# 130 if * 답안 확인
import requests 
# requests 모듈 import 에러 발생
# 원인 : requests 모듈 미설치됨
# 해결방법 : terminal 창에 [ pip3 install requests] 명령어 입력
# 참고 주소창 : https://ludere.tistory.com/57

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 변동 : 시가 - 최저  
fluctuation = float(btc['opening_price']) - float(btc['min_price']) 
open = float(btc['opening_price']) # 시가 
max = float(btc['max_price']) # 최고가

# 시가 + 변동 = n 
# n > 최고가 
# n 보다 큰 경우 : 상승장
if (open+fluctuation) > max:
    print("상승장")

# n 보다 작은 경우 : 하락상
else:
    print("하락상")

# 결과 : 하락상