#Counter
# 가장 많은 원소 찾기
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}

for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

# print(answer[1]) # = 4
# print(answer[3])  # = 3
# print(answer[100])  # =  raise KeyError


import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0