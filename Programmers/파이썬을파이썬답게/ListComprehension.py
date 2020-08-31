#https://docs.python.org/3/reference/expressions.html?highlight=list%20comprehension#displays-for-lists-sets-and-dictionaries
mylist = [3, 2, 6, 7]

arr = [s for s in mylist if s > 3 ]
print(arr)

answer = [ i**2 for i in mylist if i %2 == 0]
print(answer)