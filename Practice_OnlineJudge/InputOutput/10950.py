num = int(input())
tmp = []
for _ in range(0,num):
    a = input().split(' ')
    tmp.append(int(a[0]) + int(a[1]))

for i in range(0,num):
    print(tmp[i])