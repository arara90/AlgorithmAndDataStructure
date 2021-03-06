# 점화식 세우기를 못함...ㅠ.ㅠ...
# D(n) = 3*D(n-2) + { 2*D(n-4) + 2*D(n-6) + 2*D(n-8) + ... + 2*D(0)}
# D(2) = 3으로 시작
# D(4) = 11, D(6) = 41 ...

def DP(n):
    # 입력값이 홀수인 경우
    if n % 2 == 1:
        return 0
    else:
        # li[n][0] : 갯수, [n][1] : { 2*D(n-4) + 2*D(n-6) + 2*D(n-8) + ... + 2*D(0)} 이 부분 저장
        li = [[0,0] for _ in range(n+1)]
        # 초기작업
        li[0] = [1, 2]
        li[2] = [3, 8]
        # 점화식 전개 : 3*D(n-2) + { 2*D(n-4) + 2*D(n-6) + 2*D(n-8) + ... + 2*D(0)}
        if n > 2:
            for i in range (4, n+1, 2):
                li[i][0] = 3*li[i-2][0] + li[i-4][1]
                li[i][1] = li[i-2][1] + (2*li[i][0])
    return li[n][0]

n = int(input())
print(DP(n))