# 파이썬 300제 문제 풀이
# 문제 풀이, 결과물 또는 답안지 확인(*) 경우

# 1. 파이썬 기초 
# print 함수 관련 문제

# 001~010 

# 001 
print(" Hello World")
# 풀이 : print로 문자열 출력
# 결과물 : Hello World

# 002
print("Mary's cosmetics")
# 풀이 : 같은 따옴표 끼리는 중복적으로 사용을 못함 -> " ' ' " (o), " "" " (x)
# 결과물 : Hello World

# 003
print('신씨가 소리질렀다. "도둑이야".')
# 풀이 : 같은 따옴표 끼리는 중복적으로 사용을 못함 -> ' " " '(o), ' '' ' (x)
# 결과물 : 신씨가 소리질렀다. "도둑이야".

# 004 //정답확인
print("C:\Windows")
# 풀이 : 운영체제(윈도우/리눅스/맥) 및 설정 폰트에 따라 역슬래시가 원화 표시로 될 수 있음 
# 결과물 : C:\Windows 

# 005
print("안녕하세요.\n만나서\t\t반갑습니다.")
# 풀이 :  \t는 탭 \n는 줄바꿈. 
# 결과물 : 
# 안녕하세요.
# 만나서          반갑습니다.

# 006
# 풀이 : print ("오늘은", "일요일") 중 print는 따옴표("")로 문자열을 구분하기 때문에 
# 따옴표(,) 사용 후 띄어쓰기 시 공백으로 구분함
# 결과물 : 오늘은 일요일

# 007
print("naver;kakao;sk;samsung")
# 풀이 : print는 공백없이 문자열을 붙여쓰면 그상태로 출력됨
# 결과물 : naver;kakao;sk;samsung

# 008
print('naver/kakao/sk/samsung')
# 풀이 : print는 공백없이 문자열을 붙여쓰면 그상태로 출력됨
# 결과물 : naver/kakao/sk/samsung

# 009 //정답확인
print("first", end=""); print("second")
# 풀이 : end를 사용하면 뒤의 출력값과 이어서(+) 출력함(줄바꿈x) 
#-> first + (end 옵션 사용) + second
# 결과물 : firstsecond

# 010
print(5/3)
# 풀이 : 파이썬에서 / 연산자는 나눗셈을 의미함
# 따라서 5를 3으로 나눈 (/) 결과가 출력됨
# 결과물 : 1.6666666666666667