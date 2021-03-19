# import heapq


# def solution(operations):
#     operlist = list(operations)
#     hq = []
#     answer = []
#     for i in operlist:
#         oper, num = i.split(" ")
#         if oper == "I":
#             heapq.heappush(hq, int(num))
#         elif oper == "D":
#             if len(hq) != 0:
#                 if num == "1":
#                     hq.pop(-1)
#                 elif num == "-1":
#                     heapq.heappop(hq)
#     if len(hq) == 0:
#         answer = [0, 0]
#     else:
#         answer.append(max(hq))
#         answer.append(min(hq))
#     return answer


import heapq


def solution(operations):
    hp = []

    for item in operations:
        c, n = item.split()
        if(c == "I"):
            heapq.heappush(hp, int(n))

        if(c == "D" and hp):
            if(int(item.split()[1]) > 0):
                hp.pop(hp.index(heapq.nlargest(1, hp)[0]))
            else:
                heapq.heappop(hp)

    if(hp):
        if(len(hp) == 1):
            return [hp[0], hp[0]]
        else:
            return [hp.pop(hp.index(heapq.nlargest(1, hp)[0])), heapq.heappop(hp)]

    else:
        return [0, 0]
