# 124 if
#입력받은 데이터 1, 2, 3
number1 = input("number1: ")
number2 = input("number2: ")
number3 = input("number3: ")

# int로 형변환
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

# 데이터1과 2,3 비교한 경우1
if number1 >= number2 and number1 >= number3:
    print(number1)

#데이터2와 1,3 비교한 경우2
elif number2 >= number1 and number2 >= number3:
    print(number2)

# 데이터3과 1,2 비교한 경우3
else:
    print(number3)

# 결과 : 
# number1: 10
# number2: 9
# number3: 20
# 20
