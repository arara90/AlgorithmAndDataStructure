#1. 한번에 최대 2명, 무제 세한
#2. 최대한 적게 사용해서 모든사람 구출
# 1~50.000
# 무게제한 40~240
# 최대 무게보다 크다
# 최대 2명

# def solution(people=[70, 50, 80, 50], limit=100):

#     answer = 0
#     isGone = [1 for _ in people ]
#     people = sorted(people, reverse=True)
#     totalWeight = 0

#     for idx in range(len(people)) : 
#         totalWeight=0
#         if(isGone[idx] == 1):
#             totalWeight = people[idx]
#             isGone[idx] = 0
#             answer += 1

#             for i in range(len(people), idx+1, -1):
#                 if(isGone[i-1] == 1):
#                     if(people[i-1]+ totalWeight > limit):
#                         break

#                     else:
#                         totalWeight += people[i-1]
#                         isGone[i-1] = 0

#     return answer


# print(solution())

#결과
# 테스트 1 〉	통과 (75.08ms, 10.3MB)
# 테스트 2 〉	통과 (3.02ms, 10.3MB)
# 테스트 3 〉	통과 (37.17ms, 10.3MB)
# 테스트 4 〉	통과 (42.75ms, 10.3MB)
# 테스트 5 〉	통과 (15.76ms, 10.3MB)
# 테스트 6 〉	통과 (2.89ms, 10.3MB)
# 테스트 7 〉	통과 (6.63ms, 10.2MB)
# 테스트 8 〉	통과 (0.17ms, 10.3MB)
# 테스트 9 〉	통과 (0.74ms, 10.2MB)
# 테스트 10 〉	통과 (26.84ms, 10.3MB)
# 테스트 11 〉	통과 (36.14ms, 10.4MB)
# 테스트 12 〉	통과 (23.82ms, 10.3MB)
# 테스트 13 〉	통과 (20.84ms, 10.3MB)
# 테스트 14 〉	통과 (3.36ms, 10.3MB)
# 테스트 15 〉	통과 (0.41ms, 10.2MB)

# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	통과 (42.43ms, 11.3MB)
# 테스트 5 〉	통과 (31.98ms, 11.2MB)

# 채점 결과
# 정확성: 75.0
# 효율성: 10.0
# 합계: 85.0 / 100.0


# 최대 2명이라는 조건 놓쳤음
# 항상 가장 무거운 사람 + 가장 가벼운 사람만 검사하면 됨
def solution(people=[70, 50, 80, 50], limit=100):
    answer = 0
    people = sorted(people, reverse=True)
    l = 0
    r = len(people)-1

    while(l <= r):
        if( people[r] + people[l] <= 100):
            r-=1
        l+=1
        answer+=1

    return answer


print(solution())

# 정확성  테스트
# 테스트 1 〉	통과 (1.21ms, 10.3MB)
# 테스트 2 〉	통과 (1.05ms, 10.2MB)
# 테스트 3 〉	통과 (0.89ms, 10.3MB)
# 테스트 4 〉	통과 (0.88ms, 10.1MB)
# 테스트 5 〉	통과 (0.48ms, 10.2MB)
# 테스트 6 〉	통과 (0.28ms, 10.2MB)
# 테스트 7 〉	통과 (0.46ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.2MB)
# 테스트 10 〉	통과 (0.89ms, 10.2MB)
# 테스트 11 〉	통과 (0.75ms, 10.2MB)
# 테스트 12 〉	통과 (0.68ms, 10.3MB)
# 테스트 13 〉	통과 (0.88ms, 10.2MB)
# 테스트 14 〉	통과 (1.20ms, 10.3MB)
# 테스트 15 〉	통과 (0.09ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (9.67ms, 10.9MB)
# 테스트 2 〉	통과 (10.82ms, 10.8MB)
# 테스트 3 〉	통과 (8.99ms, 10.8MB)
# 테스트 4 〉	통과 (9.96ms, 10.7MB)
# 테스트 5 〉	통과 (8.43ms, 10.9MB)
# 채점 결과
# 정확성: 75.0
# 효율성: 25.0
# 합계: 100.0 / 100.0