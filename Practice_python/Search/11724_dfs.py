import sys
sys.setrecursionlimit(10000)

answer = 0
node, edge = map(int, sys.stdin.readline().rstrip().split())

nodes = [[] for _ in range(node+1) ]
can_visit = [ True for _ in range(node+1)] ##방문체크

def dfs(idx):
    if(can_visit[idx]):
        can_visit[idx] = False
        for i in nodes[idx]:
            dfs(i)

# node마다 edge 정보 저장
for i in range(edge):
    start, end = map(int, (sys.stdin.readline().rstrip()).split())
    nodes[start].append(end)
    nodes[end].append(start)

    #nodes[min(start,end)].append(max(start,end))
    # 이 부분이 계속 틀렸는데 왜 이렇게 하면 안될까?...
    
for i in range(1, node+1):
    if(can_visit[i]):
        can_visit[i] = False
        answer += 1
        dfs(i)
    
print(answer)


# import sys

# sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
# N, M = map(int, input().split())
# g = [[] for _ in range(N)]
# vst = [False] * N
# c = 0
# for _ in range(M):
#     a, b = map(int, input().split())
#     g[a - 1].append(b - 1)
#     g[b - 1].append(a - 1)


# def dfs(v):
#     for w in g[v]:
#         if not vst[w]:
#             vst[w] = True
#             dfs(w)


# for i in range(N):
#     if not vst[i]:
#         vst[i] = True
#         dfs(i)
#         c += 1
# print(c)