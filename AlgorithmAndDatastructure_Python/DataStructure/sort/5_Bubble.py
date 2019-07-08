def bubbleSort(x):
    for j in reversed(range(len(x))):
        for i in range(0,j):
            if x[i] > x[i+1]:
                x[i], x[i+1]= x[i+1],x[i]
        print(x)

x = [4,2,1,6,7,3,5]
bubbleSort(x)
