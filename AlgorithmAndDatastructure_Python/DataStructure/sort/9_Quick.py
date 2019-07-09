# divide and Conquer
# randomly select a data and divide into two lists
def change(x,i,j):
    x[i],x[j] = x[j],x[i]

def Select (x,left,right):
    select_val = x[left]
    select_idx = left


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
    print(x)
    return right

def quickSort(x,pivotMethod = Select):

    def Qsort(x,first,last):
        if first < last:
            splitP = pivotMethod(x,first,last)
            Qsort(x,first,splitP-1)
            Qsort(x, splitP+1, last)
        print(x)

    Qsort(x,0,len(x)-1)



x = [5,3,8,4,9,1,6,7]
quickSort(x)
print(f'fin : {x}')


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
#
# x = [5,3,8,4,9,1,6,7]
# x = quick_sort(x)
# print(f'fin : {x}')