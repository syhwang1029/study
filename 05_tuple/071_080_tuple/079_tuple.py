# 079 tuple 언팩킹 *답안 확인
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b)

# 풀이 : 
# 예상 결과는 a, b, c 로 (오답)

# 언패킹으로 a = 'apple', b = 'banana', c = 'cake'로 언팩킹 함.
# 즉, a,b,c라는 변수 안에 temp 변수값을 재할당하는 것임.
# unpackin은 여러 개의 객체(a,b,c)를 하나의(temp)로 풀어주는 것을 말함.
# 결과 : apple banana cake