# divide and Conquer
# randomly select a data and divide into two lists
def change(x,i,j):
    x[i],x[j] = x[j],x[i]

def Select (x,left,right):
    select_val = x[left]
    select_idx = 1

    while left <= right:
         while left <= right and x[left] <= select_val:
             left += 1

         while left <= right and x[right] >= select_val:
             right -= 1

         if left <= right:
             change(x,left,right)
             left =+ 1
             right -= 1

    change(x, select_idx, right)
    return right

def quickSort(x,pivotMethod = Select):
    def Qsort(x,first,last):
        if first < last:
            splitP = pivotMethod(x,first,last)
            Qsort(x,first,splitP-1)
            Qsort(x, splitP+1, last)
        print(x)
        
    Qsort(x,0,len(x)-1)

x = [4,2,1,6,7,3,5]
quickSort(x)
print(f'fin : {x}')
