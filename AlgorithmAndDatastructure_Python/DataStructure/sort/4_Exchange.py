x = [4,2,1,6,7,3,5]
print(x)
print('=================exchangeSort===============')
def exchangeSort(x):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[j], x[i] = x[i], x[j]
                print(x)
            print(x)
        print(f'{i}회전 : {x}')

exchangeSort(x)

print('=================bubbleSort===============')


def bubbleSort(x):
    for j in reversed(range(len(x))):
        for i in range(0,j):
            if x[i] > x[i+1]:
                x[i], x[i+1]= x[i+1],x[i]
            print(x)
        print(f'{len(x) - j}회전 : {x}')

bubbleSort(x)