# 3.파이썬 문자열 
# 031~040

# 031
a = "3" #문자 3
b = "4" #뮨자 4
print(a + b) # 예상 결과 : 34 
# 풀이 : 문자열끼리 더하는 경우 숫자로 인식하지 않기 때문에 연산없이 그대로 붙여지기만 함 
# 결과물 : 34

# 032
print("Hi" * 3) # 예산 결과 : HiHiHi
# 풀이 : 문자열을 3번 곱하여 반복적으로 세번 나타남. 파이썬에서는 문자열 곱하기도 가능함.
# 결과물 : HiHiHi

# 033
print("-" * 80)# - 80개 출력 
# 풀이 : 문자열 -을 80번 곱함
# 결과물 : --------------------------------------------------------------------------------

# 034
t1 = 'python' # python java python java python java python java이 출력되야 함
t2 = 'java' 
t3= t1+" "+t2 #python + (공백) + javapython 
print(t3*4) 
# 풀이 : # * 연산자로 위 t3를 4번 곱함
# 결과물 : python javapython javapython javapython java

# 035 % formatting 메서드 중 %s, %d
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1)) 
print("이름 : %s 나이 : %d" % (name2, age2))
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13 이 출력되어야 함
# 풀이 : % formatting 중 %s는 문자열, %d는 숫자형을 나타냄
# 결과물 : 
# 이름 : 김민수 나이 : 10
# 이름 : 이철희 나이 : 13

# 036 문자열의 format( ) 메서드
name36_1 = "김민수" 
age36_1 = 10
name36_2 = "이철희"
age36_2 = 13
print("이름 : {} 나이: {} ".format(name36_1, age36_1))
print("이름 : {} 나이: {} ".format(name36_2, age36_2))
# 풀이 : format는 {}으로 글자의 위치를 정하고, format() 안에 변수를 지정함으로써 문자열 포맷이 가능함.
# 결과물 :
# 이름 : 김민수 나이: 10
# 이름 : 이철희 나이: 13

# 037 f-string
name37_1 = "김민수" 
age37_1 = 10
name37_2 = "이철희"
age37_2 = 13
print(f"이름 : {name37_1} 나이 : {age37_1}") 
print(f"이름 : {name37_2} 나이 : {age37_2}")
# 풀이 :f-string은 문자열 맨앞에 f를 붙이고 중괄호{}안에 변수명을 넣음으로써 
# print 안에 변수값인 문자열로 추가가 가능함
# 결과물 : 
# 이름 : 김민수 나이 : 10
# 이름 : 이철희 나이 : 13


# 038
# 풀이 :
samsung38 = "5,969,782,550" # 삼성전자의 상장주식수
samsung38_1 = samsung38.replace(",","") # replace 메서드로 컴마(,) 제거
samsung38_2 = int(samsung38_1) #정수로 형변환
print(samsung38_2)
# 결과물 : 5969782550

# 039 인덱싱
quarter = "2020/03(E) (IFRS연결)" # 2020/03 만 출력해야함
print(quarter[:7]) #인덱스 7번째가 03임
# 풀이 : 인덱싱로 끝을 7번째까지로 정한 후 문자열을 출력함 
# 결과물 : 2020/03

# 040 strip 메서드
samsung40 = "   삼성전자    " # 공백제거해야함
samsung40_2 = samsung40.strip() #새 변수에 strip 메서드를 사용하여 공백제거
print(samsung40_2) 
# 풀이 : strip 메서드는 공백을 제거해줌
# 결과물 : 삼성전자