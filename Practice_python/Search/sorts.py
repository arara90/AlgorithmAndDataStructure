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
    