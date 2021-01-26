# https://www.youtube.com/watch?v=aOhhNFTIeFI&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=8&t=453s

# 서로소 집합은 '무방향'그래프에서 사이클을 판별할 수 있음
# 방향 - DFS, 무방향 - 서로소

# 1. 각 간선을 하나씩 확인하며 두 노드의 루트노드를 확인합니다.
#   1) 루트노드가 서로 다르다면 두 노드에 대해 합집합 연산 수행
#   2) 같다면 Cycle 발생

# 2. 그래프에 포함되어 있는 모든 간선에 대해 1번과정 반복


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


# 간선으로 열결된 a,b 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False  # cycle발생여부

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    else:
        union_parent(parent, a, b)


if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다 ")
