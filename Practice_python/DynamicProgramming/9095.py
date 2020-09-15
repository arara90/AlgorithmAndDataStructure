import sys

a = int(sys.stdin.readline().rstrip())
nums = []
max_num = 0

for i in range(a):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    if(num>max_num):
        max_num = num
    

def solution( max_num, nums):
    answer = []
    dp_list = [ 0 for _ in range(max_num+1)]
    dp_list[0] = 0
    dp_list[1] = 1
    dp_list[2] = 2
    dp_list[3] = 4
    
    def dp(curr_num):
        if(curr_num < 4):
            return dp_list[curr_num]
        
        else:
            dp_list[curr_num] = dp(curr_num-3) + dp(curr_num-2) + dp(curr_num-1)
            return dp_list[curr_num]
  

    for curr_num in nums:
        answer.append(dp(curr_num))

    return answer

for num in solution(max_num, nums):
    print(num)