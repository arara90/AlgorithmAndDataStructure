# def solution(prices):
#     answer = [ 0 for i in prices]
#     length = len(prices)
    
#     for i,v in enumerate(prices):
#         pivot = i+1
#         while(pivot<length):
#             if((prices[pivot] < v ) or (pivot == length-1)):
#                 answer[i] =  pivot - i
#                 break
#             pivot += 1
                
#     return answer

# #     정확성  테스트
# # 테스트 1 〉	통과 (0.04ms, 10.7MB)
# # 테스트 2 〉	통과 (0.07ms, 10.7MB)
# # 테스트 3 〉	통과 (0.62ms, 10.7MB)
# # 테스트 4 〉	통과 (0.69ms, 10.9MB)
# # 테스트 5 〉	통과 (0.89ms, 11MB)
# # 테스트 6 〉	통과 (0.05ms, 10.5MB)
# # 테스트 7 〉	통과 (0.38ms, 10.8MB)
# # 테스트 8 〉	통과 (0.45ms, 10.7MB)
# # 테스트 9 〉	통과 (0.06ms, 10.7MB)
# # 테스트 10 〉	통과 (0.85ms, 10.9MB)
# # 효율성  테스트
# # 테스트 1 〉	통과 (133.58ms, 139MB)
# # 테스트 2 〉	통과 (106.23ms, 105MB)
# # 테스트 3 〉	통과 (168.33ms, 155MB)
# # 테스트 4 〉	통과 (120.38ms, 120MB)
# # 테스트 5 〉	통과 (79.49ms, 87.6MB)



#[1,3,1,1,0]
# def solution(prices = [4, 2, 3, 5, 1]):
#     answer = []
#     v_stack = [prices.pop()]
#     d_stack = [0]
    
#     while(prices):
#         v = prices.pop()
#         print('newW', v)
#         cnt = 0
        
#         for item in v_stack:
#             cnt += 1
#             print("item, v, cnt", item, v, cnt)
#             if(item < v):
#                 v_stack.append(v)
#                 d_stack.append(cnt)
#                 print(v_stack)
#                 print(item, v, "hello")
#                 break
#         else:
#             print("else")
#             v_stack.append(v)
#             print(v_stack)
#             d_stack.append(len(v_stack)-1)

#     print(v_stack, d_stack)



# solution()


def solution(prices):
    value = prices.pop()
    values = [value]
    secs = [0]

    while(prices):
        cnt = 0
        value = prices.pop()
        print('while', values, value)

        for item in values:

            cnt += 1
            print("value, item", value, item, value<item)

            if( value < item ):
                values.append(value)
                secs.append(cnt)
                print('if')
                break
            else:
                print('else')
                
        else:
            print('real')
            secs.append(cnt)
            values.append(value)


    return [item for item in reversed(secs)]

print(solution(	[2, 6, 5, 7, 3, 1]))