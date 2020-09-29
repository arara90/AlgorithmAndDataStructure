# # 운행횟수      N
# # 배차간격(분)      T
# # 정원          M 

# def toSec(time):
#         m, s = time.split(":")
#         return int(m)*60 + int(s)

# def toMin(sec):
#     m, s = divmod(sec, 60)
#     return '%02d' % m + ":"+ '%02d' % s
    
# def solution(n, t, m, timetable):
#     answer = ''
#     t *= 60
#     waitings = sorted(list(map(toSec, timetable)), reverse=True)
    
#     #셔틀 시간
#     lastTime = 11*60+59
#     startTime = 9*60
#     shuttleTime = startTime
#     currM = 0
        
#     while(n>0 and shuttleTime < lastTime):
#         if(n==1 and currM == m-1): #마지막 셔틀이고, 정원이 한명 남았으면
#             arriveAt = min(waitings[-1], shuttleTime + t) - 1
#             return toMin(arriveAt) 
        
#         else:
#             if(waitings[-1] <= shuttleTime): #다음 사람이 셔틀시간전에 와있으면
#                 waitings.pop()
#                 currM += 1
#                 if(currM == n):
#                     currM = 0
#                     n -= 1
#                     if(n==0):
#                         return toMin(shuttleTime) 


#     return answer
#https://blog.naver.com/PostView.nhn?blogId=jaeyoon_95&logNo=221904129221&categoryNo=74&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search
def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    last_time = (60*9) + (n-1)*t
    
    for i in range(n):
        if len(timetable) < m: return '%02d:%02d'%(last_time//60,last_time%60)
        if i == n - 1:
            if timetable[0] <= last_time: last_time = timetable[m-1] - 1
            return '%02d:%02d'%(last_time//60,last_time%60)
        for j in range(m-1, -1, -1):
            bus_arrive = (60*9) + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]
