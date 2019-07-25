from sys import stdin

str = list(stdin.readline())[:-1]
n = len(str)
for i in range(0,n,10):
    print(''.join(str[i:i+10]))


