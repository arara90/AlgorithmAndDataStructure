
# 문제풀이 소요시간 : 약 55분
# 지체원인 : 반복문 조건 설정,  currTime = jobs[0][0] (현재시간에 시작할게 없어도, jobs가 비워져있는 경우를 생각하지 못했음 )
import heapq


def solution(jobs=[[0, 10], [4, 10], [5, 11], [15, 2]]):

    # 작업 요청 시점으로 정렬
    jobs.sort()
    length = len(jobs)

    currHeap = []  # 현재 가능한 작업들 heap
    currTime = 0  # 현재시간
    workTime = 0  # 대기 시간을 합친 소요시간 (현재시간 - 요청시점 + 소요시간 )
    accTime = 0  # 총 소요시간

    # jpbs가 비워질때까지 수행
    while(jobs or currHeap):
        if(jobs):
            while(jobs[0][0] <= currTime):  # 현재시점 전에 들어온 요청들 heap에 저장
                requestAt, duration = jobs.pop(0)
                # (소요시간, 요청시점) 으로 순서 변경
                heapq.heappush(currHeap, (duration, requestAt))

                if(not jobs):
                    break
        
        #heap에 있는 작업 꺼내서 처리
        if(currHeap):
            curr = heapq.heappop(currHeap)
            workTime = currTime - curr[1] + curr[0]  # 현재시간 - 요청시점 + 소요시간
            accTime += workTime
            currTime = currTime + curr[0]  # 다음시점

        else:
            currTime = jobs[0][0]

    return accTime//length


print(solution())


# currTime로직에 따른 차이는 크게 없음
# currTime=jobs[0][0]                              currTime += 1
# 테스트 1 〉	통과(0.95ms, 10.1MB)        테스트 1 〉	통과(0.88ms, 10.2MB)
# 테스트 2 〉	통과(0.77ms, 10.2MB)        테스트 2 〉	통과(0.89ms, 10.2MB)  # 차이있음
# 테스트 3 〉	통과(0.78ms, 10.2MB)        테스트 3 〉	통과(0.73ms, 10.2MB)
# 테스트 4 〉	통과(0.69ms, 10.2MB)        테스트 4 〉	통과(0.64ms, 10.1MB)
# 테스트 5 〉	통과(0.86ms, 10.2MB)        테스트 5 〉	통과(0.96ms, 10.2MB)
# 테스트 6 〉	통과(0.03ms, 10.1MB)        테스트 6 〉	통과(0.04ms, 10.2MB)
# 테스트 7 〉	통과(0.61ms, 10.2MB)        테스트 7 〉	통과(0.58ms, 10.2MB)
# 테스트 8 〉	통과(0.45ms, 10.1MB)        테스트 8 〉	통과(0.43ms, 10.2MB)
# 테스트 9 〉	통과(0.17ms, 10.1MB)        테스트 9 〉	통과(0.18ms, 10.2MB)
# 테스트 10 〉	통과(0.93ms, 10.2MB)      테스트 10 〉	통과(0.91ms, 10.2MB)
# 테스트 11 〉	통과(0.02ms, 10.1MB)      테스트 11 〉	통과(0.02ms, 10.2MB)
# 테스트 12 〉	통과(0.01ms, 10.3MB)      테스트 12 〉	통과(0.02ms, 10.2MB)
# 테스트 13 〉	통과(0.02ms, 10.2MB)      테스트 13 〉	통과(0.02ms, 10.2MB)
# 테스트 14 〉	통과(0.01ms, 10.1MB)      테스트 14 〉	통과(0.02ms, 10.2MB)
# 테스트 15 〉	통과(0.02ms, 10.2MB)      테스트 15 〉	통과(0.02ms, 10.2MB)
# 테스트 16 〉	통과(0.01ms, 10.2MB)      테스트 16 〉	통과(0.02ms, 10.2MB)
# 테스트 17 〉	통과(0.01ms, 10.2MB)      테스트 17 〉	통과(0.01ms, 10.2MB)
# 테스트 18 〉	통과(0.01ms, 10.1MB)      테스트 18 〉	통과(0.01ms, 10.2MB)
# 테스트 19 〉	통과(0.01ms, 10.2MB)      테스트 19 〉	통과(0.01ms, 10.2MB)
# 테스트 20 〉	통과(0.01ms, 10.2MB)      테스트 20 〉	통과(0.01ms, 10.2MB)
