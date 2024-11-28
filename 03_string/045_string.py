# 045 endswith
file_name045 = "보고서.xlsx" # 'xlsx' 또는 'xls'로 끝나는지 확인
file_name045_endswith = file_name045.endswith("xlsx" and "xls") 
# endswith 메서드로 'xlsx' 또는(and) 'xls'로 끝나는지 확인함
print(file_name045_endswith) 
# 풀이 : endswith 메서드로 변수는 xlsx로 끝나기 때문에, False로 반환됨
# 결과 : False