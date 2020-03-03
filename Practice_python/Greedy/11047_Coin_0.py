# 문제
# # 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# #
# # 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# #
# # 입력
# # 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# #
# # 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
# #
# # 출력
# # 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
from sys import stdin

n,k = list(map(int,(stdin.readline()).split()))

# 동전 종류 초기화
coins = [ 0 for _ in range(n)]

for _ in range(n):
    coins.append(int(stdin.readline()))

###### 직접 동전입력
# coins[0] = 1
# 동전 값 넣기
# 1 5 10 50 100 500...
# for i in range(1,n):
#     if i % 2 == 0:
#         coins[i] = coins[i-2] * 10
#     else :
#         coins[i] = coins[i - 1] * 5

# print(coins)
res = 0
for coin in reversed(coins):
    tmp = int(k/coin)
    if tmp > 0:
        res += int(k/coin)
        k = k%coin
    if k == 0:
        break

print(res)





