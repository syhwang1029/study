# 046 startswith
file_name046 = "2020_보고서.xlsx" # '2020'로 시작하는지 확인
file_name046_startswith = file_name046.startswith("2020") 
# startswith 메서드로 문자열 '2020'로 시작하는지 판단함 
print(file_name046_startswith)
# 풀이 : startswith 메서드는 지정한 문자열로 시작하지 판단한 후 bool로 반환함
# 문자열 2020으로 시작되기 때문에 True로 반환됨
# 결과 : True 