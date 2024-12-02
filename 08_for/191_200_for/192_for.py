# 192 for

# 종목 리스트
# OHLC (open/high/low/close) 가격 정보
data = [
        [2000,  3050,  2050,  1980],
        [7500,  2050,  2050,  1980],
        [15450, 15050, 15550, 14900]
        ]

# a 변수에 리스트 저장
for a in data:
    # b 변수에 한요소씩 분할 후 할당
    for b in a:
        # 2000
        # print(b)

        # 수수료 0.014 %
        # 종목 가격 * 수수료
        # 2000.28
        print(b * 1.00014)

    # 반복문 한번당 마무리 구분 문자
    # "-" *5 = -----    
    print("-" * 5)


# 결과 :
# 2000.28
# 3050.427
# 2050.2870000000003
# 1980.2772
# -----
# 7501.05
# 2050.2870000000003
# 2050.2870000000003
# 1980.2772
# -----
# 15452.163
# 15052.107
# 15552.177
# 14902.086000000001
# -----