#프로그래머스

#내 답
def solution(progresses, speeds):
    answer = []
    res = []

    import math
    for p, s in zip(progresses, speeds):
        res.append(math.ceil((100-p)/s)) 

    #import math X, map사용
    # res = list(map( lambda x : -((x[0]-100) // x[1] ), list(zip(progresses, speeds))))
    
    first = res[0]
    cnt = 1
    
    for i in res[1:]:
        if(i>first):
            answer.append(cnt)
            first = i
            cnt = 1
        else:
            cnt = cnt+1
    answer.append(cnt)
            
    return answer



# 다른 사람 풀이
# pop과 반복문 같이 쓰기와 직관적인 풀이! 

def solution2(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
