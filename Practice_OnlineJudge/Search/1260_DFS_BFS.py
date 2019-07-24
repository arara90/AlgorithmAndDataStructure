## 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
## 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
## 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

## 성공! 29816KB	88ms
from sys import stdin

class Node:
    # node 초기화
    def __init__(self, data=0):
        self.data = data
        self.BFS_marked = False
        self.DFS_marked = False
        self.adjacents = []

    def addAdjacent(self, index):
        if index not in self.adjacents:
            self.adjacents.append(index)
            self.adjacents.sort()

class Graph:
    nodes = [Node(0)]
    def __init__(self,size):
        for i in range(1,size+1):
            self.nodes.append(Node(i))

    def size(self):
        print(len(self.nodes))

    #2. edge 추가
    def addEdge(self,index1, index2 ):
       a = self.nodes[index1]
       b = self.nodes[index2]

       a.addAdjacent(index2)
       b.addAdjacent(index1)

    #3. DFS(Stack 이용)
    def DFS(self,root):
        global outputs
        def visitAdacents(node):
            for i in node.adjacents:
                if self.nodes[i].DFS_marked == False:
                    # 1. 연결된 노드를 stack에 저장하기
                    stack.append(self.nodes[i])
                    # 2. mark
                    self.nodes[i].DFS_marked = True
        stack = []

        # 0.root에서 시작
        node = self.nodes[root]
        outputs.append(node.data)
        node.DFS_marked = True
        visitAdacents(node)

        #1.stack에 남는게 없을때까지 반복
        while(stack):
            # stack에서 노드꺼내기
            node = stack.pop()
            # output에 해당 노드 저장하기
            outputs.append(node.data)
            # 해당 노드에 연결된 노드들 방문
            visitAdacents(node)

        # 출력
        while (outputs):
         print(outputs.pop(0))

    # 4. BFS(Queue 이용)
    def BFS(self, root):
        global outputs
        queue = []

        def visitAdacents(node):
            for i in node.adjacents:
                if self.nodes[i].BFS_marked == False:
                    # 1. 연결된 노드를 stack에 저장하기
                    queue.append(self.nodes[i])
                    # 2. mark
                    self.nodes[i].BFS_marked = True


        # 0.root에서 시작
        node = self.nodes[root]
        outputs.append(node.data)
        node.BFS_marked = True
        visitAdacents(node)

        # 1.stack에 남는게 없을때까지 반복
        while (queue):
            # stack에서 노드꺼내기
            node = queue.pop(0)
            # output에 해당 노드 저장하기
            outputs.append(node.data)
            # 해당 노드에 연결된 노드들 방문
            visitAdacents(node)



#5. DFSR(reculsive 이용)
    def DFSR(self,node):
        global outputs
        outputs.append(node.data)
        node.DFS_marked = True

        for i in node.adjacents:
            adj_node = self.nodes[i]
            if not adj_node.DFS_marked :
                self.DFSR(adj_node)



###################### 입력 ############################
inputs = list(map(int, (stdin.readline()).split()))
Nodes_size,Edges_size, Start_index  = inputs

# 1. Node 갯수에 따른 Graph생성
g = Graph(Nodes_size)

# 2. Edge 추가
for i in range(Edges_size):
    a, b = list(map(int, (stdin.readline()).split()))
    g.addEdge(a,b)

# print("DFS")
outputs = []
g.DFSR(g.nodes[Start_index])
print(' '.join(map(str,outputs)))

# print("BFS")
outputs = []
g.BFS(Start_index)
print(' '.join(map(str,outputs)))



#수정 전 출력
# while (outputs):
#     print(outputs.pop(0),end=' ')



