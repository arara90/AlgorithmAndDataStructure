# 완전탐색
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 
# 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야하는 시각입니다.

# 00시 00분 03초
# 00시 13분 30초

# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다.

# 00시 02분 55초
# 01시 27분 45초

# 첫째 줄에 정수 N이 입력 (0 <= N <= 23)
# ex) 5 -> 11475

# 가능한 모든 시각의 경우를 하나씩 모두 세는 문제
# 24* 60*60 = 86400 으로 많지 않은 경우임


h = int(input())
count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)