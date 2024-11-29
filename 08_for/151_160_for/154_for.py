# 154 for

# 문자 리스트
strls = ["I", "study", "python", "language", "!"]
# lens 변수에 리스트 할당
for lens in strls:
    # 슬라이싱으로 세글자 가진 문자만 출력
    if lens[3:]:
        print(lens)
# 결과 :
# study
# python
# language