# https://www.youtube.com/watch?v=cswJ1h-How0&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=9
# 동빈나

# 1과 자기자신을 제외한 자연수로는 나누어떨어지지않는 자연수

import math
O(X) = > 2부터 x-1까지의 모든 자연수 확인


def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어지면
        if x % i == 0:
            return False
        else:
            return True


print(is_prime_number(4))
print(is_prime_number(7))

# 약수의 성질
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭
# ex) 16 -> 1 2 4 8 16
# -> 2*8 = 16, 8*2=16 은 대칭
# -> 따라서 모든 약수를 찾을 때, 가운데 약수(제곱근)까지만 확인
# 시간복잡도는 O(N^½)


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        return True


# 다수의 소수 판별
# 범위 내 모든 소수?
# 에라토스테네스의 체 + 약수의 성질 알고리즘
    # 1) 2부터 N의 제곱근(작은쪽)26 -> 5 까지의 모든 자연수 나열
    # 2) 남은 수 중 아직 처리하지 않은 가장 작은 소수 i 찾기
    # 3) 남은 수 중에서 i의 배수 모두 제거(i는 남긴다)
    # 4) 2,3 반복
# 시간복잡도 -> 선형에 가까울 정도로 빠르다 O(nloglogN) 100만->400만
# 메모리 많이 필요 ex) 10억

array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
