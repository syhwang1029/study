# 096 keys
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#  value 값만 생성
icecream_values = icecream.values() # value 값만 생성
icecream_list = list(icecream_values) # list로 형변환
print(icecream_list)

# 풀이 : icecream 딕셔너리를 values() 함수로 value 값만 호출하고,
# list() 함수로 list 형변환함.
# 결과 : [1200, 1200, 1800, 1500, 1000]
