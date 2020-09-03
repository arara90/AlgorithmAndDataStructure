# My Solution
def compare(dp, floor, idx):
    pre_floor = floor - 1
    
    #첫번째(메인에서 초기화했음)
    if pre_floor < 0:
        return 0
    
    # 제일 왼쪽
    elif idx == 0:
        return dp[pre_floor][idx]
        
    #제일 오른쪽    
    elif idx == len(dp[floor]) -1 :
        return dp[pre_floor][idx-1]

    else:
        left = dp[pre_floor][idx-1]
        right = dp[pre_floor][idx]
        return left if left > right else right
        #max로 간단히 쓰자

    
def solution(triangle):
    dp = [ [ 0 for _ in item ] for item in triangle]
    
    #초기화
    answer = triangle[0][0] 
    dp[0][0] = triangle[0][0] 
    
    for floor_idx, items in enumerate(triangle[1:]):
        floor = floor_idx + 1 #실제 층수
        for idx, val in enumerate(items):
            res = compare(dp, floor, idx) + val
            dp[floor][idx] = res
            answer = (answer if answer > res else res)
        
    return answer

#깔끔
def solution2(triangle):
    row = len(triangle)
    for i in range(1,row):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])


#문법공부용... 
solution2 = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])

# ㅊㅊ 
def solution3(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])