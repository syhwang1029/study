# 083 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4] #가운데 8개 값
a, *valid_score, b = scores 
print(valid_score) 

# a = 8.8, b = 9.4, valid_score = 그외
# * 로 valid_score만 언패킹함.
# 결과 : [8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]