# 080 range *답안 확인
tuple_range = tuple(range(2,100,2)) #2~98 짝수만 출력
# 범위(2시작,100끝,2간격)
print(tuple_range) 

# 풀이 : range(start, end, step) -> range(시작, 끝, 간격)
# end는 출력되지 않음(포함X)
# range 함수는 범위를 지정하여 사용하기 때문에, 
# 2에서 시작하여 100까지의 범위로 숫자 간격을 2로 설정하여 
# 예를 들어 2,4는 2+2=4+2=6.. 이런 식으로 짝수만 출력이 됨.
# 이때, 100은 범위에 포함되지 않기 때문에 출력되지 않음.

# 결과 : (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 
# 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 
# 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 
# 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)
