# 2시간 소요 ㅠㅠ
# 푸는 방법 정리&암기해서 시간 단축시키기!

# def dfs(curr):
#     nodes = graph[curr]
#     st.append(curr)
#     while(nodes):
#         nn = nodes.pop(0)
#         if(visited[nn]==0):
#             visited[nn]=1
#             dfs(nn)
#     st.pop()    
#     visited[curr]=2

# def solution(n, computers):
#     answer = 0
#     global graph, st, visited
#     graph = {}
#     st = []
#     visited = [0] * n #0-방문전 1-방문중(in stack) 2-방문완료
#     #get node connections
#     for i, nodes in enumerate(computers):
#         graph[i] = []
#         for nodeIndex, connection in enumerate(nodes):
#             if(connection==1): graph[i].append(nodeIndex)

#     #1. 첫 node 선정
#     curr=0
#     # computer 차례차례 검색(단 이미 방문한 computer는 dfs에서 체크된다.)
#     while(curr<n): # N
#         if visited[curr]==0:
#             answer+=1
#             dfs(curr)
#         curr += 1            
#     return answer

# graph 사용                             graph 미사용   
# 테스트 1 〉	통과 (0.02ms, 10.2MB)  | 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)  | 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)  | 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.3MB)  | 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)  | 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.28ms, 10.2MB)  | 테스트 6 〉	통과 (0.20ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)  | 테스트 7 〉	통과 (0.03ms, 10.4MB)
# 테스트 8 〉	통과 (0.20ms, 10.2MB)  | 테스트 8 〉	통과 (0.14ms, 10.2MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)  | 테스트 9 〉	통과 (0.10ms, 10.3MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)  | 테스트 10 〉	통과 (0.10ms, 10.2MB)
# 테스트 11 〉	통과 (0.85ms, 10.3MB)  | 테스트 11 〉	통과 (0.77ms, 10.3MB)
# 테스트 12 〉	통과 (0.81ms, 10.2MB)  | 테스트 12 〉	통과 (0.53ms, 10.3MB)
# 테스트 13 〉	통과 (0.33ms, 10.2MB)  | 테스트 13 〉	통과 (0.27ms, 10.3MB)


# graph안쓰고 짜보기
# 훨씬 빠름! (위에 테스트 결과에서 오른쪽.)
def dfs(curr, computers):
    st.append(curr)
    nodes = computers[curr]
    for computer, conn in enumerate(nodes):
        if(conn==1 and visited[computer]==0):
            visited[computer] = 1
            dfs(computer, computers)
    st.pop()
    visited[curr] = 2
                
            
def solution(n, computers):
    answer = 0
    global st, visited
    st = []
    visited = [0] * n #0-방문전 1-방문중(in stack) 2-방문완료

    # computer 차례차례 검색(단 이미 방문한 computer는 dfs에서 체크된다.)
    for curr in range(n): # N
        if visited[curr]==0:
            answer+=1
            dfs(curr, computers)
            
    return answer