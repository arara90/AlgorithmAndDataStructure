#시간초과
from queue import PriorityQueue
    
def solution(genres, plays):
    answer = []
    genreHash = {}
    
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre not in genreHash:
            genreHash[genre] = (0, PriorityQueue())
        genreHash[genre][1].put((-play, i))
        genreHash[genre] = ( genreHash[genre][0] - play,  genreHash[genre][1])

    res = sorted(genreHash.values())
    
    for album in res:
        answer.append(album[1].get()[1])
        if(album[1]):
            answer.append(album[1].get()[1])

    return answer

#PriorityQueue말고 heapq를 썼더니 통과?!
import heapq
def solution(genres, plays):
    answer = []
    genreHash = {}
    priority = []
    
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre not in genreHash:
            genreHash[genre] = (0, [])

        heapq.heappush(genreHash[genre][1], (-play, i))
        genreHash[genre] = ( genreHash[genre][0] - play,  genreHash[genre][1])

    
    res = sorted(genreHash.values())
    print(res)
    # [(-3100, [(-2500, 4), (-600, 1)]), (-1450, [(-800, 3), (-150, 2), (-500, 0)])]

    for album in res:
        answer.append(heapq.heappop(album[1])[1])
        if(album[1]):
            answer.append(heapq.heappop(album[1])[1])

    return answer


                                      # genreHash[genre][0]+play
# 나의 결과                             # sorted시 reverse=True                 #아래 sum을 이용한 정렬                #고쳐보기(sorted에서 reverse하나없애기) ..비슷     
# 테스트 1 〉	통과 (0.02ms, 10.3MB)   테스트 1 〉	통과 (0.03ms, 10.3MB)        테스트 1 〉	통과 (0.02ms, 10.2MB)  # 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)   테스트 2 〉	통과 (0.02ms, 10.2MB)        테스트 2 〉	통과 (0.02ms, 10.2MB)  # 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)   테스트 3 〉	통과 (0.02ms, 10.2MB)        테스트 3 〉	통과 (0.02ms, 10.3MB)  # 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)   테스트 4 〉	통과 (0.02ms, 10.2MB)        테스트 4 〉	통과 (0.02ms, 10.3MB)  # 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.08ms, 10.3MB)   테스트 5 〉	통과 (0.15ms, 10.3MB)        테스트 5 〉	통과 (0.11ms, 10.2MB)  # 테스트 5 〉	통과 (0.11ms, 10.2MB)     
# 테스트 6 〉	통과 (0.08ms, 10.3MB)   테스트 6 〉	통과 (0.14ms, 10.2MB)        테스트 6 〉	통과 (0.09ms, 10.3MB)  # 테스트 6 〉	통과 (0.10ms, 10.3MB)     
# 테스트 7 〉	통과 (0.05ms, 10.2MB)   테스트 7 〉	통과 (0.09ms, 10.3MB)        테스트 7 〉	통과 (0.07ms, 10.2MB)  # 테스트 7 〉	통과 (0.07ms, 10.2MB)     
# 테스트 8 〉	통과 (0.03ms, 10.3MB)   테스트 8 〉	통과 (0.06ms, 10.2MB)        테스트 8 〉	통과 (0.05ms, 10.3MB)  # 테스트 8 〉	통과 (0.05ms, 10.2MB)     
# 테스트 9 〉	통과 (0.02ms, 10.2MB)   테스트 9 〉	통과 (0.03ms, 10.2MB)        테스트 9 〉	통과 (0.03ms, 10.4MB)  # 테스트 9 〉	통과 (0.03ms, 10.3MB)     
# 테스트 10 〉	통과 (0.11ms, 10.3MB)   테스트 10 〉	통과 (0.17ms, 10.3MB)    테스트 10 〉	통과 (0.13ms, 10.2MB)  # 테스트 10 〉	통과 (0.12ms, 10.3MB)     
# 테스트 11 〉	통과 (0.02ms, 10.3MB)   테스트 11 〉	통과 (0.05ms, 10.2MB)    테스트 11 〉	통과 (0.03ms, 10.1MB)  # 테스트 11 〉	통과 (0.03ms, 10.2MB)     
# 테스트 12 〉	통과 (0.05ms, 10.3MB)   테스트 12 〉	통과 (0.08ms, 10.3MB)    테스트 12 〉	통과 (0.07ms, 10.3MB)  # 테스트 12 〉	통과 (0.07ms, 10.3MB)     
# 테스트 13 〉	통과 (0.09ms, 10.2MB)   테스트 13 〉	통과 (0.15ms, 10.3MB)    테스트 13 〉	통과 (0.11ms, 10.2MB)  # 테스트 13 〉	통과 (0.10ms, 10.2MB)     
# 테스트 14 〉	통과 (0.10ms, 10.2MB)   테스트 14 〉	통과 (0.16ms, 10.3MB)    테스트 14 〉	통과 (0.11ms, 10.2MB)  # 테스트 14 〉	통과 (0.11ms, 10.2MB)     
# 테스트 15 〉	통과 (0.02ms, 10.3MB)   테스트 15 〉	통과 (0.23ms, 10.3MB)    테스트 15 〉	통과 (0.03ms, 10.3MB)  # 테스트 15 〉	통과 (0.03ms, 10.3MB)     
     
# 다른사람풀이 (sum으로 정렬하기)
# But,,성능면에서 dict에 값 추가시마다 sum해주는 것이 더 빠르다.
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer

#고쳐보기
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
        
    genreSort =sorted(list(d.keys()), key= lambda x: -sum(map(lambda y: y[0], d[x])))
    
    for g in  genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
        
    return answer




