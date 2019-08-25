# 오답
# def solution(citations):
#     answer = len(citations)
#     citations = sorted(citations, reverse = True)
#     # [7, 6, 5, 5, 3, 1, 0]
#     for i, v in enumerate(citations, start=1):
#         if i >= v:
#             answer = i
#             break
#
#     return answer
#
# print(solution([3, 0, 6, 1, 5])) #3
# print(solution([3, 0, 6, 1, 5, 5, 7])) #4
# print(solution([0,1])) #1
# print(solution([22,42])) #2


def solution1(citations):
    l = len(citations)
    citations = sorted(citations)
    for i in range(l):
           if citations[i] >= l-i :
               return l-i



print(solution1([3, 0, 6, 1, 5])) #3
print(solution1([3, 0, 6, 1, 5, 5, 7])) #4
print(solution1([0,1])) #1
print(solution1([22,42])) #2


## 3
# citations = [3, 0, 6, 1, 5]
citations = [3, 0, 6, 1, 5, 5,5, 7]
citations.sort(reverse=True)
print(citations)                                        # [6, 5, 3, 1, 0]   # [42, 22]
print(list(map(min, enumerate(citations, start=1))))    # [1, 2, 3, 1, 0]   # [1, 2]
print(max(map(min, enumerate(citations, start=1))))     # 3                 # 2