#	29056KB	76ms

import sys

N, M, V = map(int, sys.stdin.readline().strip().split())

List = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    List[a].append(b)
    List[b].append(a)

for l in List:
    l.sort(reverse=True)


def DFS(node):
    dfs = []
    visited = [0 for i in range(N + 1)]
    stack = [node]

    while stack:
        curr = stack.pop()
        if visited[curr] == 0:
            visited[curr] = 1
            dfs.append(curr)
            stack += List[curr]

    return dfs


print(' '.join(map(str, DFS(V))))

for l in List:
    l.sort()


def BFS(node):
    bfs = []
    visited = [0 for i in range(N + 1)]
    queue = [node]

    bfs.append(node)
    visited[node] = 1

    while queue:
        curr = queue.pop(0)
        for i in List[curr]:
            if visited[i] == 0:
                visited[i] = 1
                bfs.append(i)
                queue.append(i)
    return bfs


print(' '.join(map(str, BFS(V))))