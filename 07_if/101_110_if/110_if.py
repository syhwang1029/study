# 110 if
# if_1
if True : 
    # if_2
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 풀이 : 예상 결과는  3, 5 임.
# if문(if_1) 조건은 True여서 if가 실행되고,
# 안에 있는 if문(if_2) 은 조건이 False 이기에, 
# False인 경우에만 실행되는 else문 "3"이 실행되고,
# 맨 마지막 줄에 있는 "5"는 탭간격으로 조건이 없고,
# 분기문(if, else)과 상관없이 무조건 실행됨.

# 결과 : 
# 3
# 5