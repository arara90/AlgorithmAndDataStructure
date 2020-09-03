import collections

def solution(participant, completion):
    cnt = dict(collections.Counter(participant))
    for i in completion:
        cnt[i] = cnt[i] -1
        
    for key, value in cnt.items():
        if value > 0 :    # 값이 20이면
            return key
        
    return ''

#결과
# 정확성  테스트
# 테스트 1 〉	통과 (0.08ms, 10.8MB)
# 테스트 2 〉	통과 (0.08ms, 10.9MB)
# 테스트 3 〉	통과 (0.16ms, 10.9MB)
# 테스트 4 〉	통과 (0.26ms, 11.1MB)
# 테스트 5 〉	통과 (0.25ms, 11MB)
# 효율성  테스트
# 테스트 1 〉	통과 (13.70ms, 86.7MB)
# 테스트 2 〉	통과 (20.66ms, 125MB)
# 테스트 3 〉	통과 (26.29ms, 152MB)
# 테스트 4 〉	통과 (48.03ms, 166MB)
# 테스트 5 〉	통과 (32.00ms, 166MB)



###### 다른 풀이 #########
#1 collection
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    #collections에서 -를 이용할수 있음
    return list(answer.keys())[0]

# 테스트 1 〉	통과 (0.08ms, 10.6MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.24ms, 10.9MB)
# 테스트 4 〉	통과 (0.42ms, 11.1MB)
# 테스트 5 〉	통과 (0.42ms, 11.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (24.42ms, 86.7MB)
# 테스트 2 〉	통과 (42.69ms, 125MB)
# 테스트 3 〉	통과 (46.60ms, 152MB)
# 테스트 4 〉	통과 (78.69ms, 166MB)
# 테스트 5 〉	통과 (59.44ms, 166MB)

#2 hash 함수
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        # print(hash(part))
        dic[hash(part)] = part
        temp += int(hash(part))
        
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.7MB)
# 테스트 2 〉	통과 (0.05ms, 10.7MB)
# 테스트 3 〉	통과 (0.26ms, 10.9MB)
# 테스트 4 〉	통과 (0.45ms, 11.1MB)
# 테스트 5 〉	통과 (0.46ms, 10.9MB)
# 효율성  테스트
# 테스트 1 〉	통과 (25.42ms, 86.6MB)
# 테스트 2 〉	통과 (39.02ms, 125MB)
# 테스트 3 〉	통과 (52.13ms, 152MB)
# 테스트 4 〉	통과 (57.62ms, 166MB)
# 테스트 5 〉	통과 (52.48ms, 166MB)