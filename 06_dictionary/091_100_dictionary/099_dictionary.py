# 099 zip, dict 
keys = ("apple", "pear", "peach") 
vals = (300, 250, 400)

result_zip = zip(keys, vals) # keys와 vals 묶음
# => dict() 함수 사용 시, 두 함수를 딕셔너리로 생성하기 때문에, 
# 딕셔너리 형식의 조건(key:value)이기에 두 변수만 지정해야 함. 
result = dict(result_zip) # 딕셔너리로 생성
print(result)

# 풀이 : keys 변수는 key 값, vals 변수는 value 값이 될 예정임.
# zip() 함수로 위 두 변수를 각각 key:value 형식으로 사용할 것이고,
# dict() 함수로 result 라는 딕셔너리를 생성함.
# 결과 : {'apple': 300, 'pear': 250, 'peach': 400}