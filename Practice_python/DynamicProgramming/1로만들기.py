# 동빈나 이코테 6.다이나믹 프로그래밍 (36:22)
# https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6

# 정수 X가 주어졌을 때, 사용할 수 있는 연산은 다음과 같이 4가지
# 1. X%5 == 0 이면 5로 나눕니다.
# 2. X%3 == 0 이면 3으로 나눕니다.
# 3. X%2 == 0 이면 2로 나눕니다.
# 4. X에서 1을 뺍니다.

# 정수 X가 주어졌을 때, 연산 4개를 사용해서 값을 1로 만들고자 합니다. 연산을 사용하는 횟수의 최솟값을 출력하세요
# 예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값입니다.
# 26->25->5->1

# 조건 풀이시간 20분 | 제한시간 1초 | 메모리제한 128MB
# 정수 X(1 <= X <= 30000)

n = int(input())
dp_list = [0] * (n+1)


# 나의 풀이
# 초기화
dp_list[0] = 0
dp_list[1] = 0
dp_list[2] = 1
dp_list[3] = 1
dp_list[5] = 1
inf = float('inf')


def dp(x):
    if x < 4 or x == 5:
        return dp_list[x]

    else:
        a = dp(x//5) if x % 5 == 0 else inf
        b = dp(x//3) if x % 3 == 0 else inf
        c = dp(x//2) if x % 2 == 0 else inf
        d = dp(x-1)
        dp_list[x] = min(a, b, c, d) + 1
        return dp_list[x]


print(dp(n))


# BottomUp풀이
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
