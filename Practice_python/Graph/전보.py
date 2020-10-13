# https://www.youtube.com/watch?v=acqm9mM1P6o&t=1s
# 1:05:47

# N개의 도시, 전보를 통해 메시지를 다른 도시로 전송할 수 있음
# 통로가 있어야 함.

# 어느날 C도시에서 위급 상황이 발생. 최대한 많은 도시로 메시지를 보내야함
# C에서 출발하여, 각 도시사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것입

# 각 도시의 번호, 통로 정보가 주어졌을 때,
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수, 모두 메시지를 받는 데까지 걸리는 시간?

# 풀이시간 60분 | 시간제한 1초 | 메모리제한 128MB
# 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
# (1<=N<=30,000 , 1<= M<=200,000 , 1<=C<=N)

# 둘째 줄 부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
# 이는 특정도시 X에서 다른 특정도시 Y로 이어지는 통로가 있으며, 메시지가 전될되는 시간이 Z
# (1<=X, Y<=N, 1<=Z<=1,000)

# 출력은 도시의 총 개수, 시간을 공백으로 구분한다.

# ex)
# 3 2 1
# 1 2 4
# 1 3 2

# res
#  2 4

import heapq
import sys


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for adj in graph[now]:  # adj[0]:node , adj[1]:소요시간
            cost = dist + adj[1]
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))


input = sys.stdin.readline
INF = int(1e9)


# 노드의 개수, 간선의 개수 입력
n, m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]  # 1번부터일때는 n+1

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[x].append((y, z))


dijkstra(start)

city_cnt = 0
time = 0

for i in distance:
    if i != INF:
        city_cnt += 1
        time = max(time, i)

print(city_cnt-1, time)
