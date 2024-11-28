# 038 string, replace
# 풀이 :
samsung38 = "5,969,782,550" # 삼성전자의 상장주식수
samsung38_1 = samsung38.replace(",","") # replace 메서드로 컴마(,) 제거
samsung38_2 = int(samsung38_1) #정수로 형변환
print(samsung38_2)
# 결과물 : 5969782550