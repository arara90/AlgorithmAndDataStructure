
import heapq
# 최소힙
def solution(scoville, k):
    answer = 0
    # for문으로 heappush() 하나씩 한거랑 같은 효과
    heapq.heapify(scoville)


    while scoville[0] < k:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)

        except IndexError:
            return -1

        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))



## heap는 최소힙기준,, 그렇다면 최대힙은?
## ref: https://www.daleseo.com/python-heapq/
## 힙은 튜플의 첫번째 값을 기준으로 힙이 구성되므로 이를 이용한다.
print('#########최대힙##########')
# 그런데 음수에서는 사용하지 못하네..!/.
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

print(heap)
while heap:
  print(heapq.heappop(heap)[1])  # index 1


