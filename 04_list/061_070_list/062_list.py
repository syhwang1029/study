# 062 슬라이싱
nums062 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 홀수만 출력해야 함
# [1, 3, 5, 7, 9] 으로 출력되야 함
print(nums062[::2]) # 슬라이싱으로 두개의 간격으로 문자열을 가져옴
# 풀이 : 슬라이싱은 [시작: 끝: 간격] 으로 데이터를 가져옴
# 결과 : [1, 3, 5, 7, 9]