import sys

def dfs(node):
    global nodes_from
    global node_check
    global visited
    for target in nodes_from[node]:
        if node_check[target]:
            node_check[target] = False
            visited.append(target)
            dfs(target)

def bfs(queue):
    global node_check
    global visited
    while queue:
        node = queue[0]
        del queue[0]
        for target in nodes_from[node]:
            if node_check[target]:
                node_check[target] = False
                queue += [target]
                visited.append(target)
    return visited


node_count, line_count, starting_node = map(int, sys.stdin.readline().strip().split())
nodes_from = [[] for _ in range(node_count+1)]

for _ in range(line_count):
    a, b = map(int, sys.stdin.readline().strip().split())
    nodes_from[a] += [b]
    nodes_from[b] += [a]

for node in nodes_from:
    node.sort()

# dfs
node_check = [True for _ in range(node_count+1)]
visited = [starting_node]
node_check[starting_node] = False
dfs(starting_node)
print(' '.join(map(str, visited)))

# bfs
node_check = [True for _ in range(node_count+1)]
visited = [starting_node]
node_check[starting_node] = False
print(' '.join(map(str, bfs([starting_node]))))