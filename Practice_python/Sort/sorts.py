array = [7,5,0,3,1,6,2,4,8]

##선택정렬
# N번 만큼 가장 작을 수를 찾아서 맨 앞으로 보낸다
# 전체 연산 횟수는 N + (N-1) + (N-2) + ... + 2 = (N^2 + N - 2 ) / 2 
# 즉 O(N^2)

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]


##삽입정렬
# O(N^2) 
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
# 최선의 경우 (이미 정렬된 상태) O(N)
for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

## 퀵정렬
# 기준데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적으로 가장 많이 사용되는 정렬 알고리즘
# 병합 정렬과 더불어 대부분의 언어의 정렬 라이브러리의 근간이 되는 알고리즘(C, java, python 표준 정렬라이브러리)
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)으로 설정

# 이상적인 경우 분할이 절반씩 일어난다면 전체 연산횟수로 O(NlogN) 평균
# 최악의 경우 O(N^2) 
# 피벗값에 따라 편향된 분할이 될 수 있다 ex) 첫번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해 퀵 정렬을 수행하면?
# 단 표준 라이브러리는 NlogN을 항상 보장한다.

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left += 1
        
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right -= 1

        if(left>right): #엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않는다면 작은데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

        #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)   
    

def quick_sort_python(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)



## 계수정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작
# 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능
# 데이터의 계수가 N, 데이터(양수) 중 최댓값이 K일때, 최악의 경우에도 수행시간 O(N+K)를 보장
# 시간복잡도, 공간복잡도 = O(N+K )

# 떄로는 심각한 비효율성 (0, 999,999로 단 두개만 존재하는 경우?)
# 따라서, 계수 정렬은 동일한 값을 가지는 데이터가 여러ㅏ개 등장할 때 효과적으로 사용할 수 있다.
# ex) 성적 - 1~100까지의 한정된 데이터 범위를 갖고, 한 점수를 여러명의 학생이 받음. 다량의 학생 데이터를 처리해야할 때.



#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)

#O(N)
for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

#count = K 만큼 확인, 다만 안쪽 반복문의 최종 수행횟수는 N 따라서, O(N+K)
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= '')



## 수행시간 비교
import time
from random import randint
array=[]
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
array.sort()
end_time = time.time()

print("수행시간: ", end_time - start_time)

 




