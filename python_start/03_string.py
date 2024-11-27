# 3.파이썬 문자열 
# 문자열은 슬라이싱 기능과 다양한 메서드를 제공함
# - 슬라이싱 : 문자열에서 여러 글자를 가져오는 것 // [ : : ] 사용
# - 인덱싱 : 문자열을 한글자만 가져오는 것 // [] 사용

# 021~030

# 021 인덱싱
letters = 'python' #첫번째 p, 세번째 t
print(letters[0], letters[2])
# 풀이 : 인덱싱은 0부터 시작하기 때문에 인데스 기준으로 p는 0번, t는 3번 인덱스임
# 결과물 : p t

# 022 슬라이싱
license_plate = "24가 2210" #뒤에서 4자리는 2210
print(license_plate[-4::]) 
# 풀이 : 슬라이싱은 [시작:끝:간격]로 표기 되는데, -4를 사용하는 경우 뒤자리 부터 시작하여 4가리 2210을 가져옴
# 결과물 : 2210

# 023 슬라이싱 //인덱싱이 아니라 슬라이싱을 활용해야 편의성이 좋아짐
string23 = "홀짝홀짝홀짝" #홀만 호출
# print(string23[0], string23[2], string23[4]) ##인덱싱
print(string23[::2]) #슬라이싱
# 풀이 : 슬라이싱을 사용하여 두간격 사이의 글자인 홀만 가져옴
# 결과물 : 
## 인덱싱 홀 홀 홀
# 홀홀홀

# 024 슬라이싱
string24 = "PYTHON" #거꾸로 출력
print(string24[::-1])
# 풀이 : 슬라이싱은 마이너스(-)를 활용하는 경우 뒷자리 글자부터 출력됨, 
# ::-1 은 글자간격을 나타내기 때문에 1글자씩 즉 NOHTYP로  출력됨
# 결과물 : NOHTYP

# 025 문자열 치환 *정답확인
phone_number25 = "010-1111-2222" # 하이푼(-) 제거
print(phone_number25.replace("-", " ")) # replace 메서드 사용하여 하이푼(-) 제거 후 띄어쓰기 적용
# 풀이 : replace 메서드를 사용하면 문자열의 일부를 치환할 수 있음(문자열은 수정 불가능)
# 결과물 : 010 1111 2222

# 026
phone_number26 = "010-1111-2222" # 01011112222가 출력되어야 함 
print(phone_number26.replace('-', ''))
# 풀이 : replace 메서드 사용하여 하이푼(-)만 제거함
# 결과물 : 01011112222

# 027 *정답확인
url27 = "http://sharebook.kr" #설명 : 도메인 kr만 출력
url27_split =url27.split('.') #. 제거
print(url27_split[-1]) #인덱싱을 사용하여 뒤에서 0,1번째인 kr만 출력됨
# 결과물 : kr

# 028
# lang = 'python' 
# lang[0] = 'P' 
# print(lang) #문자열은 수정 불가능 
### 28번은 에러 발생으로 주석처리함
# 풀이 : 인덱싱으로 할이 불가능 하기 때문에 P로 수정 시도 시 에러 발생
# 결과물 : 
# raceback (most recent call last):
#   File "/Users/hwangseoyoung/Documents/aid/python/study/python_start/03_string.py", line 56, in <module>
#     lang[0] = 'P'
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment

# 029 *정답확인
string29 = 'abcdfe2a354a32a' # 예상 Abcdfe2A354A32A
string29_2 = string29.replace('a', 'A') # 소문자 a를 대문자 A로 변경
print(string29_2)
# 풀이 : replace 함수는 문자열 변경을 변경해줌 -> 함수명.replace('변경 전','변경 후')
# 결과물 : Abcdfe2A354A32A

# 030 *정답확인
string30 = 'abcd'
string30_1 = string30.replace('b', 'B') #소문자 b를 대문자 B로 변경
print(string30_1) # 'abcd' -> 'aBcd'로 예상 
# 풀이 : replace 함수를 활용하여 aBcd로 예상됨(오답)
# 정답지 : 문자열은 변경할 수 없기 때문에 변형없이 그대로 출력됨
#  replace 메서드는 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줌
# 결과물 : abcd

## aBcd로 변경하고 싶은 경우
# string30 = 'abcd'
# string30_1 = string30.replace('b', 'B') #새로운 변수 string30_1에 변수값이 할당되기 때문에, 변경이 가능함.
# print(string30_1) 
