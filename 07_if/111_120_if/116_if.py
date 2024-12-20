# 116 if 
times = input("시간을 입력하세요. (단, 00:00 형태로 입력하세요.)")

if times[-2:] == "00": 
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 풀이 : input() 함수로 데이터를 받음.
# times[-2:] 는 슬라이싱으로 반댓방향으로 2번째 인덱스를 받은 데이터의 자리로 지정함. 
# 12:00 을 입력값으로 받은 경우, 00이 반댓방향 2번째 인덱스 번호를 뜻함.
# 입력값 뒷에서 2번째 자리에 00이 들어간 경우 True로 "정각 입니다.",
# 00이 아닌 경우 False로 "정각이 아닙니다."가 출력됨.

# 결과 : 
# 1. 입력값 : 12:00
# 시간을 입력하세요. (단, 00:00 형태로 입력하세요.)12:00
# 정각 입니다.

# 2. 입력값 : 12:30
# 시간을 입력하세요. (단, 00:00 형태로 입력하세요.)12:30
# 정각이 아닙니다.