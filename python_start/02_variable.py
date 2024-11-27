# 2. 파이썬 변수
# 변수는 자주 사용되는 값을 바인딩함 
# - 바인딩 : 자료형, 변수명, 변수값 등등 각각 구체적인 값을 할당하는 과정

# 011~020
# 011
samsung = 50000 #삼성전자
stock = 10 #주식 10주
tot = samsung * stock #총 평가금액
# 풀이 : samsung 이라는 변수에 50000 숫자형 할당 
# stock 라는 변수에 10 숫자형 할당 
# tot 이라는 변수에 삼성전자와 주식 곱하여 총 평가금액 합산
# 결과물 : 500000 

# 012
street = 298000000000000 #시가총액
present = 50000 # 현재가
PER = 15.79 # PER
print("street: "+str(street)) 
print(present)
print(PER)
# 풀이 : street의 변수값이 int형이기 때문에, p
# rint 안에 문자열(street:) 을 추가할 경우에는 sting 타입 변형(str(street)))이 필요함.
# 결과물 :
# street: 298000000000000
# 50000
# 15.79

# 013
s = "hello"
t = "python"
print(s+"!"+ " "+t)
# 풀이 :print 안에서 중간에 느낌표(!)와 공백("")을 추가하여 hello! python과 이어 조건에 할당함
# 결과물 : hello! python

# 014
print(2 + 2 * 3 )
# 풀이 : 2 + 2 * 3 는 연산자 우선순위(+다음 *순으로 연산)에 따라 
# 2*3 = 6 + 2 = 8로 결과를 예상함  
# 결과물 : 8

# 015 
a = "132"
print(type(a))
# 풀이 : type 함수를 활용하여 a 변수가 string 이라는 타입을 판별함
# 결과물 : <class 'str'>

# 016
num_str = "720" #문자열 
num_int = int(num_str) #정수형(int)으로 형변환
print(num_int+1, num_int) #형변환 확인용 숫자추가(+1)
# 풀이 : int 함수로 str을 정수로 변환함
# 결과물 : 721 720

# 017
num = 100 #정수형
num_str2 = str(num)  #문자열(str)로 형변환
print("문자열 100 : "+num_str2) #형변환 확인용 글자추가
# 풀이 : str 함수로 int를 문자열로 변환함
# 결과물 : 문자가된 100 : 100


# 018
num_str3 = "15.79" #문자열
num_float1 = float(num_str3) #실수형(float)으로 형변환
print(1.0+num_float1) #형변환을 위한 숫자추가(+1.0)
# 풀이 : float 함수로 문자열을 실수형으로 변환함
# 결과물 : 16.79

# 019
year = "2020" #2020년도 #문자열
year_int = int(2020) # 정수로 형변환
year2019 = year_int-1 #2019년도 (2020년도 기준-1년도)
year2018 = year_int-2 #2018년도 (2020년도 기준-2년도)
year2017 = year_int-3 #2017년도 (2020년도 기준-3년도)
print(year2019) 
print(year2018)
print(year2017)
# 풀이 :int 함수로 str을 정수형으로 형변환
# 결과물 :
# 2019
# 2018
# 2017

# 020
month = 48584 #에이컨이 월 48,584원 ## 숫자형 사용시 콤마(,) 사용금지 주의
interest = 36 #무이자 36개월
tot2 = month * interest # 48,584원 * 36개월 = 총금액
print(tot2) ##변수명 중복확인
# 풀이 : * 연산자를 활용하여 월 금액과 이자 개월을 서로 곱하여 총액을 계산함
# 결과물 : 1749024