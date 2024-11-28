# 027 split( *답안확인
url27 = "http://sharebook.kr" #설명 : 도메인 kr만 출력
url27_split =url27.split('.') #. 제거
print(url27_split[-1]) #인덱싱을 사용하여 뒤에서 0,1번째인 kr만 출력됨
# 결과물 : kr