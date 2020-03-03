from sys import stdin
n = int(stdin.readline())
for _ in range(n):
    tmp = list(map(int, stdin.readline().split(',')))
    print(tmp[0]+tmp[1])