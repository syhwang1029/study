# 159 for *답안 확인

# 디렉토리 리스트
filels = ['intra.h', 'intra.c', 'define.h', 'run.py']
# file 변수에 리스트 할당
for file in filels:
    # '.'으로 요소 분할
    filesp = file.split(".")
    # 1번째 인덱스에 "h" 가 있는 요소만 출력
    if filesp[1] == "h":
        print(file)
      
# 결과 :
# intra.h
# define.h        