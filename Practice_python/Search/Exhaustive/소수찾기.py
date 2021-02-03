# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3


#나의풀이
from itertools import permutations
import math

def isSosu(num): #primeNumber ㅋㅋㅋ
    sqrt = float(math.sqrt(num))
    i = 2

    while(i<=sqrt):
        if(num%i==0): return False
        else: i+=1

    return True
    
    
def solution(numbers="011"):
    answer = 0
    myList = []
    
    # 모든 부분집합구하기
    for i in range(1, len(numbers)+1):
        tmp = map(''.join, permutations(list(numbers), i))
        tmpList = list(map(int, tmp))
        myList.extend(tmpList)
        myList = list(set(myList))

    # mySet = set()
    # for i in range(1, len(numbers)+1):
    #     tmp = map(''.join, permutations(list(numbers), i))
    #     mySet |= set(map(int, tmp))

    for num in myList:
        if(num<2):
            pass
        else:
            if(isSosu(num)):
                answer+=1
    
    return answer

# 테스트 1 〉	통과 (0.08ms, 10.3MB)
# 테스트 2 〉	통과 (3.36ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.81ms, 10.4MB)
# 테스트 5 〉	통과 (3.78ms, 10.5MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.09ms, 10.4MB)
# 테스트 8 〉	통과 (3.84ms, 10.5MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (9.91ms, 10.5MB)
# 테스트 11 〉	통과 (1.33ms, 10.3MB)
# 테스트 12 〉	통과 (0.25ms, 10.2MB)

#다른사람 #1
# 로직자체보다는 set 연산자의 활용을 볼 것,
# from itertools import permutations
# def solution(n='17'):
#     a = set()
#     for i in range(len(n)):
#         print(a)
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    
#     print(a)
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))


#     return len(a)

#테스트 1 〉	통과 (0.81ms, 10.4MB)
# 테스트 2 〉	통과 (76.43ms, 44.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (51.62ms, 19.9MB)
# 테스트 5 〉	통과 (251.16ms, 145MB)
# 테스트 6 〉	통과 (0.05ms, 10.4MB)
# 테스트 7 〉	통과 (1.01ms, 10.4MB)
# 테스트 8 〉	통과 (717.81ms, 280MB)
# 테스트 9 〉	통과 (0.91ms, 10.4MB)
# 테스트 10 〉	통과 (349.99ms, 51MB)
# 테스트 11 〉	통과 (26.18ms, 13.8MB)
# 테스트 12 〉	통과 (5.70ms, 13.2MB)


#다른 사람2 
#itertools 없이 모든 부분집합 구하기
# def getAllCombination(numbers, numList, leftCipher):
#     '''
#     numbers : 총 숫자카드 list
#     numList : 가능한 숫자 배열 list
#     leftCipher : 남은 자릿수
#     '''

#     # 현재 가능한 숫자 배열 list를 기준으로 추가가 가능한 숫자들은 찾는다. 
#     newNumList = [[]]


#     for li in numList:
#         for i in numbers:
#             if i in li and li.count(i) <= numbers.count(i) - 1:
#                 tmp = li[:]
#                 tmp.append(i)
#                 newNumList.append(tmp)
#             if i not in li:
#                 tmp = li[:]
#                 tmp.append(i)
#                 newNumList.append(tmp)

#     leftCipher -= 1

#     if leftCipher == 0:
#         return newNumList
#     else:
#         return getAllCombination(numbers, newNumList, leftCipher)


print(solution())