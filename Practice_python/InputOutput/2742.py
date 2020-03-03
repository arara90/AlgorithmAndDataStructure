from sys import stdin
num = int(stdin.readline())
for i in range(num,0,-1):
    print(i)


# 아래가 더 빠름
# import sys
# print("\n".join(str(i) for i in range(int(sys.stdin.readline()),0,-1)))
