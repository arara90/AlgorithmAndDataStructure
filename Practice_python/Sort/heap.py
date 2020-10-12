import heapq
# minheap이 default #O(logN) #최대 O(nlogn)
# 표준 라이브러리의 병합정렬, 퀵정렬 기반의 정렬과 동일한 시간 복잡도

# 오름차순 힙 정렬(heap sort)


def asc_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# 내림차순 힙 정렬(heap sort)
def desc_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


result = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(desc_heapsort(result))

result = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(asc_heapsort(result))
