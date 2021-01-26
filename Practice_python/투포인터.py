
# https://www.youtube.com/watch?v=cswJ1h-How0&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=9
# 동빈나

# 투포인터(two pointer)알고리즘
# 리스트에 순차적으로 접근해야 할 때, 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
# 흔히 2,3,4,5,6 번 학생을 지목해야할 때 간단히 2번부터 7번까지의 학생이라고 부름
# 리스트에 담긴 데이터에 순차적으로 접근할깨 시작점과 끝 점 2개의 점으로 접근할 데이터의 범위 표현


# example 1
#  특정한 합을 가지는 부분 연속 수열 찾기
#  N개의 자연수로 구성된 수열이 있습니다.
#  합이 M인 부분 연속 수열의 개수를 구해보세요
#  수행시간 제한은 o(N)

# 1. 시작점과 끝점이 첫번째 원소의 인덱스를 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면 카운트
# 3. M보다 작다면 end를 증가
# 4. 크거나 같다면, start를 1 증가
# 5. 모든 경우 확인할 때까지 2번부터 4번까지의 과정 반복

n = 5  # 데이터의 개수 N
m = 5
data = [1, 2, 3, 2, 5]  # 전체 수열

cnt = 0
interval_sum = 0
end = 0

for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분합이 m일 때, cnt 증가
    if interval_sum == m:
        cnt += 1

    interval_sum -= data[start]

print(cnt)


# 구간합(접두사합PrefixSum)

# n개의 정수로 구성된 수열이 있습니다.
# m개의 쿼리 정보가 주어집니다. 각 쿼리는 left, right로 구성됩니다.
# 각 쿼리에 대하여 [left, right] 구간에 포함된 데이터들의 합을 출력해야 합니다.
# 수행시간 제한은 O(n+m)

# -> 접두사합 : 배열의 맨앞부터 특정 위치까지의 합을 미리 구해 놓는 것
# N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P애 저장합니다.
# 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[right] - P[left-1]

# 10 20 30 40 50
# 0 10 30 60 100 150 left=1 , right=3 ==> P[3] - P[0] = 60
# O(K) 상수시간 처리속도

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)


left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])
