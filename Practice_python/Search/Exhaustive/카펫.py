# 35분 소요
# 수학 공식 이용하는 풀이 참고

# def solution(brown, yellow):
#     answer = []
#     cases = []
#     total = brown + yellow

#     #case 구하기 (약수)
#     i =  3  #3이상부터
#     m, n = divmod(total, i)

#     while(i <= m):
#         if(n==0):
#             cases.append([m,i])
#         i+=1
#         m, n = divmod(total, i)

#     #조건에 맞는 case 선별
#     for item in cases:
#         w, h = item
#         if(yellow == (w-2) * (h-2)):
#             answer = item
#             break
    
#     return answer

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.25ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.15ms, 10.1MB)
# 테스트 7 〉	통과 (0.30ms, 10.2MB)
# 테스트 8 〉	통과 (0.24ms, 10.3MB)
# 테스트 9 〉	통과 (0.30ms, 10.2MB)
# 테스트 10 〉	통과 (0.32ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.3MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)


# 더 간편한 풀이
# def solution(brown, red):
#     total = brown + red
#     for n in range(1, total+1):
#         if total%n != 0:
#             continue
#         m = total//n
#         if (n-2)*(m-2) == red:
#             return sorted([n, m], reverse = True)

#이용해서 내꺼수정

def solution(brown, yellow):
    answer = []
    total = brown + yellow

    #case 구하기 (약수)
    h =  3  #3이상부터
    w, n = divmod(total, h)

    while(h <= w):
        if(n==0):
            if(yellow == (w-2) * (h-2)):
                answer = [w, h]
                break
        h+=1
        w, n = divmod(total, h)

    return answer