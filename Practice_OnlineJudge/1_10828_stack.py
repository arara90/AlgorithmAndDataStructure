#################################################################################################

# 시작 - 18:35 /  목표 -19:00 / 종료 - 19:56...................
# 1. li.pop()으로 써야하는데 li.pop으로 써서 계속 built-in 오브젝트가 반환되었던건데 pop이라는 입력이 안되는 줄 알고 매우 삽질함..ㅠ.ㅠ
# 2. 출력 형식 안맞춤
# 3. stack_answer보다 0.04 초 느린데 왜 때문일까? ( 812ms / 816ms )
#   1. 함수? 호출 지워보기 : 816ms ->  no matter
#   2. split? 안하고 answer처럼 해보기 : 812ms .. -> split을 반복하면 시간적인 패널티가 있네!
#   3. insert( index, data) 써보기 : 헐 804ms -> 0.12초 단축함.
#       1. insert가 주 요인일까, pop 대신 직접 delete 해준 것이 요인일까? 그게 그건가..
#           -> append로 바꾸고 직접 delete해주기 : 804ms
#            -> pop 내장함수를 사용하지 않고, delete를 직접해준 것이 영향이 큰 듯!

#######################################원본############################################################
# # stack : LIFO
#
# def do(commend, li):
#     cmds = commend.split(' ')
#     # push면 append하고 함수 나가기
#
#     size = len(li)
#     if cmds[0] == 'push':
#         li.append(int(cmds[1]))
#
#     else:
#         if cmds[0] == 'pop':
#             if size ==0:
#                 print(-1)
#             else:
#                 print(li.pop())
#
#         elif cmds[0] == 'top':
#             if size == 0:
#                 print(-1)
#             else:
#                 print(li[-1])
#
#         elif cmds[0] == 'empty':
#             print(int( not li ))
#
#         elif cmds[0] == 'size':
#             print(size)
#
# # 명령어 수 입력
# n =int(input())
#
# # list
# li = []
# cms = []
# for i in range(0,n):
#     user_input = input()
#     do(user_input, li)
#


#################################수정 3-2#####################################################
#
# def do(commend, li):
#     size = len(li)
#     if commend == 'pop':
#         if size == 0:
#             print(-1)
#         else:
#             print(li.pop())
#     elif commend == 'top':
#         if size == 0:
#             print(-1)
#         else:
#             print(li[-1])
#
#     elif commend == 'empty':
#         print(int(not li))
#
#     elif commend == 'size':
#         print(size)
#
#     elif commend[0:4] == 'push':
#         li.append(int(commend.split()[-1]))
#         #li.insert(0,str[5:]) #이거를 쓰면 top도 항상 li[0]을 쓸 수 있고
#         # , 원래 stack의 의미랑 더 비슷해짐
#
#
# # 명령어 수 입력
# n = int(input())
#
# # list
# li = []
# cms = []
# for i in range(0, n):
#     user_input = input()
#     do(user_input, li)

# ###################### 3-3수정 : insert써보기 -> top[0] / pop로직 -> print 후에 delete해줘야함 #########
# def do(commend, li):
#     size = len(li)
#     if commend == 'pop':
#         if size == 0:
#             print(-1)
#         else:
#             print(li[0])
#             del li[0]
#
#     elif commend == 'top':
#         if size == 0:
#             print(-1)
#         else:
#             print(li[0])
#
#     elif commend == 'empty':
#         print(int(not li))
#
#     elif commend == 'size':
#         print(size)
#
#     elif commend[0:4] == 'push':
#         li.insert(0,int(commend.split()[-1]))
#
#
# # 명령어 수 입력
# n = int(input())
#
# # list
# li = []
# cms = []
# for i in range(0, n):
#     user_input = input()
#     do(user_input, li)


###################### 3-3-1수정 : append하고 pop에서 delete 직접하기 804ms#########
# def do(commend, li):
#     size = len(li)
#     last = size - 1
#
#
#     if commend == 'pop':
#         if size == 0:
#             print(-1)
#         else:
#             print(li[last])
#             del li[last]
#
#     elif commend == 'top':
#         if size == 0:
#             print(-1)
#         else:
#             print(li[-1])
#
#     elif commend == 'empty':
#         print(int(not li))
#
#     elif commend == 'size':
#         print(size)
#
#     elif commend[0:4] == 'push':
#         li.append(int(commend.split()[-1]))
#
#
# # 명령어 수 입력
# n = int(input())
#
# # list
# li = []
# cms = []
# for i in range(0, n):
#     user_input = input()
#     do(user_input, li)
