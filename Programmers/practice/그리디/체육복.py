def solution(n, lost, reserve):
    answer = 0
    res = [ 1 for _ in range(n)] # res=[1] * n
    
    #초기 상태
    for idx, val in enumerate(res):        
        if (idx + 1) in lost:
            res[idx] = res[idx] - 1

        if (idx + 1) in reserve:
            res[idx] = res[idx] + 1

    #0인 경우 주위에서 빌려오기
    for idx, val in enumerate(res):  
        if res[idx] == 0:
            if(idx > 0 and res[idx-1] ==2):
                res[idx-1] -= 1
                res[idx] = 1
                answer+=1
                continue
            
            elif(idx < len(res)-1 and res[idx+1] ==2 ):
                res[idx+1] -= 1
                res[idx] = 1
                answer+=1
                continue
                
        else: answer+=1

    return answer
