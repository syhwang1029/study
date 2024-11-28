# 095 keys
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# key 값만 생성
icecream_keys = icecream.keys() # key 값만 생성
icecream_list = list(icecream_keys) # list로 형변환
print(icecream_list)

# 풀이 : icecream 딕셔너리를 keys() 함수로 key 값만 호출하고,
# list() 함수로 list 형변환함.
# 결과 : ['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']
