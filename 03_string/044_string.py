# 044 endswith
file_name044 = "보고서.xlsx" # 'xlsx'로 끝나는지 확인
file_name044_endswith  = file_name044.endswith("xlsx") # endswith 메서드로 xlsx로 끝나는지 판단함
print(file_name044_endswith)
# 풀이 : endswith 메서드는 지정한 문자열로 끝나는지 판단한 후 bool로 반환함
# 참인 경우는 True이고, 거짓인 경우는 False임
# xlsx로 끝나기 때문에 True로 반환됨
# 결과 : True