#주의할 점:
# 좌표체계와 행렬의 전환
# 조건문의 순서. ( 가장자리에 웅덩이가 있는 경우 생각못했음)
# dpbag을 안쓰는 경우 시간초과된다.

def solution(m=4, n=3, puddles=[[2,2]]):
    answer = 0
    dpbag = [ [-1 for _ in range(0,n+1)] for _ in range(0,m+1) ]

    #n이 rowm m이 col
    def dp(i, j):
        
        if [i,j] in puddles :
            dpbag[i][j] = 0
            dp(i-1, j) + dp(i, j-1)
            return 0
        
        elif i == 0 or j == 0:
            dpbag[i][j] = 0
            return  0

        elif i == 1 and j == 1:
            dpbag[1][1] = 1
            return 1
        
        elif dpbag[i][j] < 0:
            dpbag[i][j] = dp(i-1, j) + dp(i, j-1)
            return dpbag[i][j]
        
        else:
            return dpbag[i][j]
        
    dp(m,n)
    print(dpbag)

    return dpbag[m][n] % 1000000007


print(solution(	4, 3, [[3, 1], [1, 3]]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 9.6MB)
# 테스트 2 〉	통과 (0.04ms, 9.61MB)
# 테스트 3 〉	통과 (0.10ms, 9.49MB)
# 테스트 4 〉	통과 (0.12ms, 9.64MB)
# 테스트 5 〉	통과 (0.21ms, 9.7MB)
# 테스트 6 〉	통과 (0.22ms, 9.67MB)
# 테스트 7 〉	통과 (0.36ms, 9.62MB)
# 테스트 8 〉	통과 (0.41ms, 9.48MB)
# 테스트 9 〉	통과 (0.19ms, 9.63MB)
# 테스트 10 〉	통과 (0.07ms, 9.45MB)
# 효율성  테스트
# 테스트 1 〉	통과 (9.89ms, 9.86MB)
# 테스트 2 〉	통과 (2.92ms, 9.81MB)
# 테스트 3 〉	통과 (3.75ms, 9.68MB)
# 테스트 4 〉	통과 (5.46ms, 9.64MB)
# 테스트 5 〉	통과 (4.33ms, 9.88MB)
# 테스트 6 〉	통과 (8.08ms, 9.9MB)
# 테스트 7 〉	통과 (4.94ms, 9.68MB)
# 테스트 8 〉	통과 (6.82ms, 9.68MB)
# 테스트 9 〉	통과 (7.34ms, 9.83MB)
# 테스트 10 〉	통과 (5.24ms, 9.67MB)



#다른 사람 풀이
# 훨씬 빠름 ㅜㅜ 

# def solution(m,n,puddles):
#     grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
#     if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
#         for a, b in puddles:
#             grid[b][a] = -1                #미리 -1로 체크
#     grid[1][1] = 1
#     for j in range(1,n+1):
#         for k in range(1,m+1):
#             if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
#                 continue
#             if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
#                 grid[j][k] = 0
#                 continue
#             grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

#     return grid[n][m]

# #     정확성  테스트
# # 테스트 1 〉	통과 (0.01ms, 9.53MB)
# # 테스트 2 〉	통과 (0.02ms, 9.38MB)
# # 테스트 3 〉	통과 (0.03ms, 9.46MB)
# # 테스트 4 〉	통과 (0.07ms, 9.5MB)
# # 테스트 5 〉	통과 (0.08ms, 9.52MB)
# # 테스트 6 〉	통과 (0.06ms, 9.39MB)
# # 테스트 7 〉	통과 (0.06ms, 9.53MB)
# # 테스트 8 〉	통과 (0.13ms, 9.46MB)
# # 테스트 9 〉	통과 (0.06ms, 9.45MB)
# # 테스트 10 〉	통과 (0.03ms, 9.57MB)
# # 효율성  테스트
# # 테스트 1 〉	통과 (3.37ms, 9.89MB)
# # 테스트 2 〉	통과 (1.52ms, 9.45MB)
# # 테스트 3 〉	통과 (1.72ms, 9.5MB)
# # 테스트 4 〉	통과 (2.29ms, 9.75MB)
# # 테스트 5 〉	통과 (2.29ms, 9.5MB)
# # 테스트 6 〉	통과 (3.05ms, 9.7MB)
# # 테스트 7 〉	통과 (1.68ms, 9.37MB)
# # 테스트 8 〉	통과 (2.32ms, 9.67MB)
# # 테스트 9 〉	통과 (2.47ms, 9.59MB)
# # 테스트 10 〉	통과 (2.73ms, 9.63MB)