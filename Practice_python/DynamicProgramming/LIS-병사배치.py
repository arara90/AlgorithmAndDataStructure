# 증가하는 부분수열 (<-> 감소하는 부분 수열)
# 0 <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
# https://jason9319.tistory.com/113 - 이분탐색으로도 풀어보기

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 최장 증가 부분 수열 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 dp테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야 하는 병사의 최소 수 출력
print(n-max(dp))


# 7
# 15 11 4 8 5 2 4
