#063 슬라이싱
nums063 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 짝만 출력해야 함
# [2, 4, 6, 8, 10] 으로 출력되야 함
print(nums063[1::2]) # 슬라이싱으로 1번째 인덱스인 2로 시작하여 두 간격인 문자열을 가져옴
# 풀이 : 슬라이싱은 [시작: 끝: 간격] 으로 데이터를 가져옴
# 결과 : [2, 4, 6, 8, 10]