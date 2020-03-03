from sys import stdin

n = int(stdin.readline())
num = list(stdin.readline())[:n]

print( sum(list(map(int, num))) )