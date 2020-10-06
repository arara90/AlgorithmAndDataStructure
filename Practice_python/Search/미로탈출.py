# N*M 직사각형 형태의 미로에 여러마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 시작 위치는 (1,1)이며 미로의 출구는 (N,M)에 있고, 한 번에 한 칸씩 이동할 수 있습니다.
# 이 때 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있습니다.
# 탈출을 위해 움직여야 하는 최소 칸의 개수를 구하세요.( 시작 칸과 마지막 칸을 모두 계산에 포함합니다.)

# (4 <= N, M <= 200), 시작와 마지막 칸은 항상 1

# 예시 
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우 무시
            if nx<0 or nx >=n or ny<0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]
            


print(bfs(0,0))