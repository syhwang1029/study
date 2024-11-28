# 100 zip, dict
date = ['09/05', '09/06', '09/07', '09/08', '09/09'] #key 값
close_price = [10500, 10300, 10100, 10800, 11000] # value 값
close_zip = zip(date, close_price) # key, value로 사용 예정
close_table = dict(close_zip) # close_table 딕셔너리 생성
print(close_table)

# 풀이 : date 변수는 key 값으로, close_price 변수는 value 값으로 사용 예정임.
# zip() 함수로 위에 두 변수를 하나로 묶음.
# dict() 함수로 close_table 딕셔너리를 생성함.
# 결과 : {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}