from bisect import bisect_left, bisect_right
# 순차탐색 - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진탐색 - 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# - 이진탐색은 시작, 끝, 중간점을 이용해 탐색 범위를 설정한다.

# 단계마다 탐색 범위를 2로 나누므로 연산 횟수는 log2N에 비레, 따라서 O(logN)보장


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점 > 찾는 값이면 왼쪽 확인
    elif(array[mid] > target):
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)


# n(원소의개수)과 target(찾고자하는값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")

else:
    print(result+1)


# while start <= end:
# mid = (start+end) // 2
# if array[mid] == target:
#     return mid
# elif array[mid] > target:
#     end = mid - 1
# else:
#     start = mid + 1
# return None

# 이진 탐색 라이브러리
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))  # 2
print(bisect_right(a, x))  # 4

# 값이 특정 범위에 속하는 데이터 개수 구하기


def count_by_range(a, left_value, right_value):
    r_idx = bisect_right(a, right_value)  # 8 , 6
    l_idx = bisect_left(a, left_value)  # 6, 0
    return r_idx - l_idx


b = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(b, 4, 4))  # 2
print(count_by_range(b, -1, 3))  # 6


# 정렬된 배열에서 특정 수의 개수 구하기(O(logN)으로 구하기, 일반적인 선형은 시간초과 )
# [1,1,2,2,2,2,3], x = 2 --> res = 4
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

# 값이 x인 원소 존재하지 않는다면
if count == 0:
    print(-1)

else:
    print(count)
