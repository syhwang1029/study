# 056 두 개의 리스트 하나로 합치기
lang1 = ["C", "C++", "JAVA"] # lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트 생성 
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#'] 출력되야 함
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2 # 하나의 변수에 리스트1 lang2 , 리스트2 lang2 서로 합침 
print(langs)
# 풀이 : 리스트끼리는 서로 합치기가 가능함
# 결과 : ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']