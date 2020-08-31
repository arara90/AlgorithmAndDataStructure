# 문자열 정렬하기 - ljust, center, rjust
# 이번 강의에서는 문자열을 좌측/가운데/우측 정렬하는 법을 배워봅니다. 예시)

# '가나다라               ' # 좌측정렬
# '               가나다라' # 우측 정렬
# '       가나다라        ' # 가운데 정렬

s = '가나다라'
n = 7

print(s.ljust(n)) # 좌측 정렬
print(s.center(n)) # 가운데 정렬
print(s.rjust(n)) # 우측 정렬