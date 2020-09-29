# # # '%10.2f' %'%10.2f' %


# # def solution(S):
# #     if(S.find('aaa')>=0):
# #         return -1

# #     elif(S=='aa'):
# #         return 0

# #     else:
# #         s_list = list(S)
# #         ans =''
# #         cnt = 0

# #         for idx, item in enumerate(s_list):
# #             if(idx==0):
# #                 if(item=='a'):
# #                     ans = 'a' + item
# #                     cnt += 1
# #                 else:
# #                     ans = 'aa' + item
# #                     cnt += 2

# #             elif(item == 'a'):
# #                 if(ans[-2:]=='aa'):

# #                     print('continue')
# #                     continue
# #                 tmp =  item + 'a'
# #                 cnt += 1
# #                 ans += tmp

# #             else:
# #                 tmp = item + 'aa'
# #                 cnt += 2
# #                 ans += tmp
# #             print( idx, item, ans, ans[-2:], cnt, 'end' )

# #     print(cnt)
# #     return ans

# # print('fy', solution('dog'))
# # print('fy', solution('aabab'))
# # '%10.2f' %'%10.2f' %
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    if(S.find('aaa')>=0):
        return -1

    elif(S=='aa'):
        return 0

    else:
        s_list = list(S)
        ans = 'aa'
        cnt = 0
        for idx, item in enumerate(s_list):
            if(idx==0):
                if(item=='a'):
                    ans = 'a' + item
                    cnt += 1
                else:
                    ans = 'aa' + item
                    cnt += 2

            if(item == 'a'):
                if(ans[-2:]=='aa'):
                    continue

                tmp = item + 'a'
                cnt += 1

            else:
                tmp = item + 'aa'
                cnt += 2
            ans += tmp

        return cnt


# def solution(S):
    
#     if(S.find('aaa')>=0):
#         return -1

#     elif(S=='aa'):
#         return 0

#     else:
#         s_list = list(S)
#         ans =''
#         cnt = 0

#         for idx, item in enumerate(s_list):
#             if(idx==0):
#                 if(item=='a'):
#                     ans = 'a' + item
#                     cnt += 1
#                 else:
#                     ans = 'aa' + item
#                     cnt += 2
#             else:
#                 tmp = ans[-2:] + item + 'a'
                
#                 if(tmp == 'aaa'):
#                     continue
#                 elif(tmp[-2:]=='aa'):
#                     cnt += 1
#                     ans += item + 'a'
#                 else:
#                     cnt += 2
#                     ans += item + 'aa'
#     print(cnt)

#     return ans

print('fy', solution('dog'))
print('fy', solution('aabab'))


#  실수..
# map으로 각인덱스별로 저장 한 후, 이미 있는 값이면 return...속도줄임

#  def checkLetter(a,b):
#     for idx, item in enumerate(zip(a,b)):
#         print(item[0], item[1] )
#         if(item[0]==item[1]):
            
#             return idx

#     return -1


# def solution(S):
#     # write your code in Python 3.6
#     for i in range(0, len(S)-1):
#         for j in range(i+1, len(S)):
#             res = checkLetter(S[i], S[j])
#             if(res > -1):
#                 return [i, j, checkLetter(S[i], S[j])]
#     return []

# print(solution(['zzzz', 'ferz', 'zdsr', 'fgtd']))



# def solution(A):
#     cnt = 0
#     tmp = [ i+1 for i in range( len(A) )]
#     print(tmp)
#     print(sorted(A))
#     for t, a in zip(tmp, sorted(A)):
#         cnt += abs(a-t)

#     print(cnt)



# solution([6, 2, 3, 5, 6, 3])
# solution([1,2,1])
# solution([2,1,4,4])