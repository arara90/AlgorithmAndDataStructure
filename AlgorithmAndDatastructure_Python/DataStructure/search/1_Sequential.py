def sequentialSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return False

x = [4,2,1,6,7,3,5]
print(sequentialSearch(x,5))