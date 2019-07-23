# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# 그리고 Quick or Merge 복습해보자
#
# python의 sort는 default로

####################### 성공 #######################3
from sys import stdin
num = int(stdin.readline())
arr=[]
for i in range(num):
    arr.append(int(stdin.readline()))

print(*sorted(arr),sep='\n')
#
# #####################  내장 sort안쓰고 quicksort구현해보기 -- 시간초과/메모리초과 T.T #####################
# ###### 시간초과?!
# ###### rand 지우면 메모리 초과 T.T
#
# import random
# # 최악의 경우를 피하기 위함
# def select_pivot(arr):
#     if len(arr) > 3:
#         # s = random.sample(arr, 3)
#         pivot = int( (arr[0] + arr[1] + arr[2]) / 3)
#         return pivot
#     else :
#         return arr[0]
#
# #quick정렬 사용
# def quick_sorted(arr):
#     if len(arr) > 1 :
#         # 기준값 선택
#         pivot = select_pivot(arr)
#         left, mid, right = [], [], []
#
#         for i in range(0, len(arr) ):
#             if arr[i] < pivot:
#                 left.append(arr[i])
#             elif arr[i] > pivot:
#                 right.append(arr[i])
#             else:
#                 mid.append(arr[i])
#
#         # print(quick_sorted(left) + mid + quick_sorted(right))
#         return quick_sorted(left) + mid + quick_sorted(right)
#
#     else:
#         return arr
#
# ########################## quicksort이용 : vinc88 /	69264kb	4768ms	 ################################################3
# from sys import stdin
# n = int(stdin.readline())
# lst = []
# for i in range(n):
#     lst.append(int(stdin.readline()))
#
#
# def quickSort2(lst):
#     def sort(low, high):
#         if high <= low:
#             return
#
#         # 기준 원소 정하기(partition나누기)
#         mid = partition(low, high)
#
#         #기준보다 작은 애들 정렬
#         sort(low, mid - 1)
#
#         #기준보다 큰 애들 정렬
#         sort(mid, high)
#
#
#
#     def partition(low, high):
#
#         # 중간 위치에 있는 원소를 pivot으로 지정
#         pivot = lst[(low + high) // 2]
#
#         while low <= high:
#             while lst[low] < pivot:
#                 low += 1
#
#             while lst[high] > pivot:
#                 high -= 1
#
#             if low <= high:
#                 lst[low], lst[high] = lst[high], lst[low]
#                 low, high = low + 1, high - 1
#         return low
#
#     return sort(0, len(lst) - 1)
#
#
#
#
# quickSort2(lst)
# for i in range(n):
#     print(lst[i])
