#050 rstrip 
data050 = "039490     " # 오른쪽 공백 제거
data050_rstrip = data050.rsplit() # rsplit 메서드로 오른쪽 공백을 제거함
print(data050_rstrip)
# 풀이 : rstlit 메서드는 오른쪽 공백()을 제거해줌
# 결과 : ['039490']