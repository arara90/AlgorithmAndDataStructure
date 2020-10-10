# 동빈나 이코테 6.다이나믹 프로그래밍 (52:38)
# https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6


# n*m 의 금광이 있습니다.
# 채굴자는 첫번째 열부터 출발하여 금을 캐기 시작합니다. 맨처음에는 첫번째 열의 어느 행에서든 출발할 수 있습니다.
# 이후에 m-1번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동합니다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하세요

# 풀이시간 30분 | 시간제한 1초 | 메모리제한 128mb
# 첫째줄 : 테스트 케이스 T (1<=T<=1000)
# 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1<=n, m<=20)
#                 둘째 중에 n*m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1<=각위치에매장된 금의 개수 <=100)
# 출력 : 테스트 케이스마다 체굴자가 얻을 수 있는 금의 최대 크기 (테스트 케이스틑 줄바꿈으로 구분)



# def getRes(n=3, m=4, array=[
#     1, 3, 3, 2, 
#     2, 1, 4, 1,
#     0, 6, 4, 7]
#     ):

#     num_map = [[]] * m
#     # for i in range(m):
#     #     num_map[i] = [ array[i+m*j] for j in range(n) ]
    
#     return(num_map)


# print(getRes())
# print(getRes(4,4,[1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]))

# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


## 풀이
# dp[i][j] = array[i][j] + max(dp[i-1][j-1] , dp[i][j-1], dp[i+1][j-1] )


for tc in range(int(input())):
    n,m = map(int, input().split())
    array =list(map(int, input().split()))

    #다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0

    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    #다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i==0: left_up = 0
            else: left_up=dp[i-1][j-1]

            #왼쪽 아래에서 오는 경우
            if i==n-1: left_down = 0
            else: left_down=dp[i+1][j-1]

            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
