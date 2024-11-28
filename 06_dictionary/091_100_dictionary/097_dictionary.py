# 097 sum
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 총합
icecream_value = icecream.values() # value 값만 생성
icecream_sum = sum(icecream_value) # 총합 연산
print(icecream_sum) 

# 풀이 : icecream 딕셔너리를 values() 함수로 value 값만 호출하고,
# sum() 함수로 합계를 구함. (이때, value 값은 전체 숫자형이라 연산이 가능함.)
# 결과 : 6700