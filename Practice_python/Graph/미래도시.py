# https://www.youtube.com/watch?v=acqm9mM1P6o&t=1s
# (1:01:00)

# 미래도시의 회사들 1~N , 특정 회사끼리 서로 도로를 통해 연결
# 방문 판매원 A는 현재 1번에 있고, X번 회사에 방문해 물건을 판매하고자 한다.

# 특정 회사에 도착하기 위해 회사끼리 연결된 도로를 이용해야한다.
# 연결된 2개의 회사는 양방향으로 이동할 수 있다. 연결되어 있다면 1의 시간으로 이동할 수 있다

# A는 기대하던 소개팅에 참석하고자 하는데, K번 회사에 존재한다.
# X번 회사에 방문 하기 전에 먼저 소개팅 상대의 회사에 찾아가서 커피를 마실 예정이다.
# 따라서, A는 1->k->X 로 가능한 빠르게 이동하는 것이 목표다.

# A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

# 조건
# 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.
# (1<=N,M<=100)
# 둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
# M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다.(1<=K<=100)

# 최소이동시간을 출력하고, 도달할 수 없다면 -1을 출력한다.


# 5 7 (N,M)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5 (X,K)
# res:3


# 풀이
# N이 최대 100개이므로 플로이드 워셜 이용해도 효율적
# 1번 노드에서 X까지의 최단 거리 + X에서 K까지의 최단거리를 나누어 생각하여 계산


INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
