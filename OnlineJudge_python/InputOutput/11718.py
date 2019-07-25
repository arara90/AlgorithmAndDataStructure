from sys import stdin
for line in stdin:
    print(line, end='')

#  이거는 안되넹..!!
# from sys import stdin
# while True:
#     try:
#         print(stdin.readline(), end='')
#     except EOFError:
#         break

# 이거는 되고!!
# while True:
#     try: print(input())
#     except EOFError:
#         break
