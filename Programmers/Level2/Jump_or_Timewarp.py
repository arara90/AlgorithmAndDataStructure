# 효율성 0 점...ㅠ.ㅠ .. 다 구해서 그럴까?

############## for문 ##############
# def solution(n):
#     global tmp_list
#     tmp_list = [0 for _ in range(0, n)]
#     tmp_list[0:2] = [0, 1, 1]
#
#     for i in range(0, n+1):
#         if i < 3:
#             #print('i<3', i, tmp_list[i] )
#             pass
#
#         else :
#             if (i % 2 == 0):
#                 tmp_list[i] = min(tmp_list[int(i/2)], tmp_list[i-1]+1)
#             else:
#                 tmp_list[i] = tmp_list[i-1]+1
#
#             #print('i>3', i, tmp_list[i])
#
#     ans = tmp_list[n]
#     print(tmp_list)
#     return ans
#
# print(solution(5000))


############## reculsive ##############
# import sys
# #print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
#
# def reculsive(i):
#     # print(i)
#     if i < 3:
#         return tmp_list[i]
#
#     elif tmp_list[i] != 0:
#         return tmp_list[i]
#
#     else :
#         if (i % 2 == 0):
#             tmp_list[i] = min(reculsive(int(i/2)), reculsive(i-1)+1)
#             return tmp_list[i]
#
#         else:
#             tmp_list[i] = reculsive(i-1)+1
#             return tmp_list[i]
#
# def solution(n):
#     global tmp_list
#
#     # 초기화
#     tmp_list = [0 for _ in range(0, n)]
#     tmp_list[0:2] = [0, 1, 1]
#     ans = reculsive(n)
#     return ans
#
# print('sol:', solution(5000))
# print(tmp_list)

##############  이진법 이용 ##############
### divmod 함수 (몫, 나머지)
# def solution(n):
#     ans = 0
#     while (n != 0):
#         n, b = divmod(n, 2)
#         ans += b
#     return ans
#
# print('sol:', solution(5000))

### 진법 변환 후 1이 몇개있는지 세기
# 진법변환 함수 : int,bin, oct, dec, hex
# https://sarc.io/index.php/development/857-python-bin-oct-dec-hex

def solution(n):
    return list(bin(n)).count('1')
