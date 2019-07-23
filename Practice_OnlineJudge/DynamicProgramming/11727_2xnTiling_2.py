# num = int(input())
# li = [0 for _ in range(0, num)]
# # 초기화
# li[0:2] = [0,1,3]
#
# def DP(num):
#     global li
#     if (li[num] == 0) & (num > 2):
#         li[num] = DP(num-2) * 2 + DP(num-1)
#     return li[num]
#
# DP(num)
# print(li[num] % 10007 )

#### for문
n = int(input())
d = [0, 1, 3]

for i in range(3, n + 1):
    d.append((d[i - 1] + d[i - 2] * 2) % 10007)

print(d[n] % 10007)