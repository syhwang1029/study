# 121~130

# 121 if
# 입력받은 데이터
users = input("단어를 입력하세요. ")

if users.islower(): # 대/소문자 판별
    print(users.upper())# True인 경우 (소문자)
else: 
    print(users.lower()) # False인 경우(대문자)

# 결과
# 1. 대문자를 소대자로 변경 (True)
# 단어를 입력하세요. HI
# hi

# 2. 소문자를 대문자로 변경 (False)
# 단어를 입력하세요. user
# USER

# 3. 한글인 경우
# 단어를 입력하세요. 안녕    
# (공백)

