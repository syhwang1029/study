# 158 for

# 디렉토리 리스트
filels = ['hello.py', 'ex01.py', 'intro.hwp']
# splis 변수에 리스트 할당
for splis in filels:
    # '.'으로 요소 분할
        file = splis.split('.')
        # 한요소 덩어리당 인덱스로 치기 때문에,
        # ['hello', 'py'] 는 'hello'가 0번, 'py' 1번 인덱스임.
        # 그리하여 0번 인덱스인 맨앞 요소들만 출력됨 
        
        # 첫번째 요소(0번 인덱스)만 출력
        print(file[0])
        
# 결과 : 
# hello
# ex01
# intro