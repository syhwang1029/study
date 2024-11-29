# 160 for

# 파일 리스트
filels = ['intra.h', 'intra.c', 'define.h', 'run.py']
# file 변수에 리스트 할당
for file in filels:
    # "."으로 요소 분할
    filesplit = file.split(".")
    # 1번 인덱스 요소에 "h" 또는 "c" 가 있는 경우만 출력
    if (filesplit[1] == "h") or (filesplit[1] == "c"):
         print(file)
# 결과 :
# intra.h
# intra.c
# define.h