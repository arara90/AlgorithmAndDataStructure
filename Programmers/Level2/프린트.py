def solution(priorities=[1, 1, 9, 1, 1, 1], location=0):
    answer = 0
    lp = [(l,p) for l, p in enumerate(priorities)] 


    while(lp):
        flag = 0
        curr = lp.pop(0)

        for item in lp:
            if(curr[1] < item[1]): #더큰값존재
                lp.append(curr)
                flag = 1
                break
        
        if(flag):
            continue
        
        else:
            answer += 1
            if(curr[0] == location ):
                break


    return answer


print(solution())