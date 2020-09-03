# 나의 답 : DP로 풀었음
def solution(numbers, target):
    tree = [ [0]*(2**num) for num in range(0, len(numbers))]
    tree[0][0] = numbers[0]
    
    for Idx, row in enumerate(tree[1:]):
        rowIdx = Idx + 1
        for columnIdx in range(len(row)):
            q, m =  columnIdx // 2,  columnIdx % 2

            if(m>0):
                tree[rowIdx][columnIdx] = tree[rowIdx-1][q] - numbers[rowIdx]
            else:
                tree[rowIdx][columnIdx] = tree[rowIdx-1][q] + numbers[rowIdx]
                
    res = list(map(abs, tree[-1]))
    return res.count(target)


# 아래 sol2 보다 공간은 덜 썼으나 초기 테스트에서만 빨랐다가 아래 케이스로 갈 수록 훨씬 느려진다. (n^2)
# 테스트 1 〉	통과 (262.86ms, 36.8MB)
# 테스트 2 〉	통과 (259.24ms, 33.5MB)
# 테스트 3 〉	통과 (0.39ms, 9.51MB)
# 테스트 4 〉	통과 (1.45ms, 9.49MB)
# 테스트 5 〉	통과 (8.80ms, 9.95MB)
# 테스트 6 〉	통과 (0.81ms, 9.55MB)
# 테스트 7 〉	통과 (0.42ms, 9.55MB)
# 테스트 8 〉	통과 (2.62ms, 9.65MB)


#itertools이용
from itertools import product
def solution2(numbers, target):
    l = [(x, -x) for x in numbers] #[(1, -1), (2, -2), (3, -3)]
    print(*l) #(1, -1) (2, -2) (3, -3)
    #print(list(product(*l))) #[(1, 2, 3), (1, 2, -3), (1, -2, 3), (1, -2, -3), (-1, 2, 3), (-1, 2, -3), (-1, -2, 3), (-1, -2, -3)]
    s = list(map(sum, product(*l)))
    return s.count(target)

solution2([1,2,3], 6)

# 테스트 1 〉	통과 (267.67ms, 33.9MB)
# 테스트 2 〉	통과 (261.51ms, 33.5MB)
# 테스트 3 〉	통과 (0.29ms, 9.53MB)
# 테스트 4 〉	통과 (1.21ms, 9.59MB)
# 테스트 5 〉	통과 (7.91ms, 10.3MB)
# 테스트 6 〉	통과 (0.59ms, 9.56MB)
# 테스트 7 〉	통과 (0.29ms, 9.53MB)
# 테스트 8 〉	통과 (2.02ms, 9.69MB)

#DFS로 풀기
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution3(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

# 더 느리다?
# 테스트 1 〉	통과 (402.38ms, 9.48MB)
# 테스트 2 〉	통과 (404.77ms, 9.5MB)
# 테스트 3 〉	통과 (0.81ms, 9.41MB)
# 테스트 4 〉	통과 (2.04ms, 9.63MB)
# 테스트 5 〉	통과 (13.14ms, 9.46MB)
# 테스트 6 〉	통과 (1.28ms, 9.49MB)
# 테스트 7 〉	통과 (0.75ms, 9.48MB)
# 테스트 8 〉	통과 (3.93ms, 9.51MB)