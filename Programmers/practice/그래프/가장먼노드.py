#계속 실패했었다... 문제는 min-max 부분에 있었다.  (11번째줄)  nodes[min(item)].append(max(item))
# \그냥 a,b 양쪽으로 두니 빠르고, 모두 잘 처리됨.. 왜일까. 양방향인데..
from collections import deque

def solution(n, edge):
    answer = 0

    #nodes에 edge 정보저장
    nodes = [ [] for _ in range(n+1) ]
    for item in edge:
        # nodes[min(item)].append(max(item))
        a,b = item
        nodes[a].append(b)
        nodes[b].append(a)

    #방문노드표시
    visited = [ 0 for _ in range(n+1) ]
    visited[0] = 1
    visited[1] = 1

    #BFS
    currQ = deque([1])
    nextQ = deque([])
    
    while(len(currQ)>0):
        currNode = currQ.popleft()
        for nextNode in nodes[currNode]:
            if( visited[nextNode] < 1):
                visited[nextNode] = 1 #visited Node 표시
                nextQ.append(nextNode) # 연결된 next level의 노드 저장

        if(len(currQ)==0): #현재 level의 노드 모두 방문
            if(len(nextQ)>0):  # 다음 level에 노드가 있으면
                answer = len(nextQ) # 다음 level에 몇개의 노드가 있는지 저장
                currQ = nextQ   # 다음 레벨 노드 정보를 currQ로 저장
                nextQ = deque() # nextQ 초기화
                
    return answer

# print('1---', solution(8, [[3,6], [5,3], [2,7], [3,2], [1,4], [3,1], [1, 2],[5,8]]))
# print('2===', solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# # 7
# print('3===', solution(17, [[1,2],[1,3],[2,4],[2,5],[3,6],[3,7],[6,8],[6,9],[8,10],[9,11],[7,12],[7,13],[13, 14],[13, 15],[15, 16],[15, 17]]))
# # 4
# print('4===', solution(7, [[1, 2],[1, 3],[2, 4],[2, 5],[3, 6],[3, 7]]))

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.28ms, 10.3MB)
# 테스트 5 〉	통과 (1.09ms, 10.5MB)
# 테스트 6 〉	통과 (1.98ms, 10.8MB)
# 테스트 7 〉	통과 (17.78ms, 16.9MB)
# 테스트 8 〉	통과 (25.34ms, 20.3MB)
# 테스트 9 〉	통과 (24.28ms, 20MB)

