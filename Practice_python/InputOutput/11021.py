from sys import stdin
n = int(stdin.readline())

for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    print(f'Case #{i+1}: {tmp[0]+tmp[1]}')