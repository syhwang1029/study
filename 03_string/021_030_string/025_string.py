# 025 문자열 치환 *정답확인
phone_number25 = "010-1111-2222" # 하이푼(-) 제거
print(phone_number25.replace("-", " ")) # replace 메서드 사용하여 하이푼(-) 제거 후 띄어쓰기 적용
# 풀이 : replace 메서드를 사용하면 문자열의 일부를 치환할 수 있음(문자열은 수정 불가능)
# 결과물 : 010 1111 2222