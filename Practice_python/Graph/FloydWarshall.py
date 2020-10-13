# 플로이드 워셜

# 나동빈 7.최단경로알고리즘
# https://www.youtube.com/watch?v=acqm9mM1P6o&t=1s 42분

# 모든 노드에서 다른 모든 노드까지의 최단 경로 모두 계산
# 다익스트알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
#     다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정 불필요
# 2차원 테이블에 최단 거리 정보 저장
# DP에 속함

# 시간복잡도 - - O(N^3)
# 노드의 개수가 N개일때 알고리즘 상으로 N번의 단계 수행
#   각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려함.
# 노드의 개수가 적을 때 사용하고 아닌 경우는 다익스트라(500*500*500 > 1억 .. 500개도 많다.)

# 각 단계마다 특정한 노드 k를 거쳐가는 경우 확인
#    a->b 최단 거리보다 a->k->b가 더 짧은지 검사
# 점화식
# D(ab) = min(D(ab), D(ak) + D(kb))


INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트 (그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신에게 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k]+graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 infinity출력
        if graph[a][b] == INF:
            print('infinity')
        else:
            print(graph[a][b], end=" ")

    print()
