# 246 module *답안 확인

# 모듈 가져오기 
import time 
import datetime

while True:
    now = datetime.datetime.now()
    # 현재 시간에서 1초당 시간 값 호출
    time.sleep(1)
    # 결과값 출력
    print(now)

# 결과 :
# 2024-12-01 17:32:03.168861
# 2024-12-01 17:32:04.178955
# 2024-12-01 17:32:05.186813
# 2024-12-01 17:32:06.235869
# 2024-12-01 17:32:07.237554
# 2024-12-01 17:32:08.244883