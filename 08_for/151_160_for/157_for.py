# 157 for *답안 확인

# 동물 리스트
animal = ['dog', 'cat', 'parrot']

# uppers 변수에 리스트 할당
for uppers in animal:
    # 첫글자만 인덱싱 
    anls = uppers[1]
    # 대문자로 변환
    anup = anls.upper()
    # 첫글자만 대문자 + 나머지 뒷글자
    # A + arrot = Aarrot
    print(anup+uppers[1:])
    #print(anup, uppers[1:])
# 결과 : 
# Oog
# Aat
# Aarrot