import heapq
#기본은 min

#미해결....
def solution(jobs):
    jobs.sort()
    size = len(jobs)
    start, end, accTime, slicingIdx = 0, 0, 0, 0
    minheap = []
    
    while( len(minheap) or slicingIdx < size):
        #1. 처리중 들어온 명령들 item pop하여 대기힙에 적재
        # print('start jobs', jobs) 
        print('w', 'end =', end, minheap, jobs[slicingIdx:] )
        for idx in range(slicingIdx, len(jobs)):
            print(jobs[idx])
            t, d = jobs[idx]

            if( t >= end ):
                print('fin')
                if(idx==0):
                    slicingIdx = idx + slicingIdx + 1
                else:
                    slicingIdx = idx + slicingIdx
                print(slicingIdx)
                break
            else:
                print('else')
                slicingIdx = idx + slicingIdx

            heapq.heappush(minheap,(d, t))
            print('heap', minheap)
        # del jobs[0:sl+icingIdx]
        # print('del jobs', jobs)                
        # print('heap', heap)

        #2. 대기힙에 들어온 아이 중 가장 적은 t 뽑기
        if(len(minheap)>0):
            hd,ht = heapq.heappop(minheap)
            start = end 
            end = end + hd 
            accTime = accTime + (end - ht)             
            # print('heappop', heap)
        
    answer = int(accTime / size)
    print(answer)

    return answer

print(solution([[0, 3], [4, 3], [10, 3]]))


# l = [[0, 3], [1, 9], [2, 6]]
# print(l[0:0])