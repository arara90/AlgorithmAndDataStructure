def solution(n, times):
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
        # print(answer, left, right, mid, upper)
        if(upper):
            #주어진 시간이 충분하면 시간을 줄여본다
            right = mid - 1
            answer = mid if answer > mid else answer
        else:
            #주어진 시간이 부족하면 시간을 늘려본다
            left = mid + 1
        
    return answer