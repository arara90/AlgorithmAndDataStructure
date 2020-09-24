# 입국심사 기다리는 사람수 n 1~1,000,000,000
# 각 심사관이 한명을 심사하는데 걸리는 시간 times 시간 (1~1,000,000,000) , 심사관( 100,000 )명 이하

# times [7, 10]
# 1분당 7명을 처리할수 있음. -> 30(분) * 1/7 = 30/7 -> 30분 동안 처리할 수 있는 일(입국심사대상)
# 30/7+30/10 = 30분 동안 둘이 처리할 수 있는 인원

# 6번케이스만 통과가 되지 않았는데 while 조건에 left와 right가 같은 경우를 뺏다.
# 그런 경우 
# answer, left, right, mid, upper
#11 1 10 5 True
# 5 1 4 2 False
# 5 3 4 3 False
# 5

# 11 1 10 5 True
# 5 1 4 2 False
# 5 3 4 3 False
# 5 4 4 4 True
# 4

def solution(n=5, times = [1,1,10]):
    answer =  max(times) * n + 1
    left = 1
    right = max(times) * n
    # print(left, right )
    

    def isPossible(n, mid, times):
        #주어진 시간(mid)안에 n명을 처리할 수 있으면 True
        res = 0
        for time in times:
            res += mid // time
        return res >= n
    
    while(left <= right):
        mid = ( left + right ) // 2
        upper = isPossible(n, mid, times)
        print(answer, left, right, mid, upper)
        if(upper):
            #주어진 시간이 충분하면 시간을 줄여본다
            right = mid - 1
            answer = mid if answer > mid else answer
        else:
            #주어진 시간이 부족하면 시간을 늘려본다
            left = mid + 1
        
     
    return answer

print(solution(5, [1,1,10])) #3
print(solution(6,[8,10])) #30
print(solution(6,[7,10])) #28
print(solution(6, [7,10])) # 28
print(solution(6, [6,10])) # 24
print(solution(6, [8,10])) # 30
print(solution(6, [4,10])) # 20
print(solution(11, [3,4,10])) # 18
print(solution( 5, [1, 2])) # 4 -> 6번케이스

