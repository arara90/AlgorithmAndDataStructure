#에라토스테네스의 체
# 루트 n 까지만 나누어서 떨어지면 소수가 아니다.

#1. 비트연산을 이용한 모든 부분집합 구하기
# https://blog.naver.com/PostView.nhn?blogId=kmh03214&logNo=221702095617&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# def powerset(s):
#     mask = [ 1 << i for i in range(len(s)) ] #len(s)=5면 -> [1,2,4,8,16] // [1, 10, 100, 1000, 10000] (이진수)
#     for i in range( 1 << len(s)):   ## 2^5 -> 32만큼 , 즉 부분집합의 개수만큼 돌게된다.
#         yield [ss for ss, mask in zip(s, mask) if mask&i]  ##( (1,1) / (2,2) / (3,4) / (4,8) / (5,16) => 1,2,3,4,5


    

# for power  in powerset([1,7]):
#     print(power)

from itertools import permutations

#에라토스테네스 체 안쓰고 sqr만 적용
def isPrimeNumber(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True

print(isPrimeNumber(18))



#에라토스테네스 적용
def solution(n):
    a = set()

    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))   # set에서 | 합집합, &교집합, - 차집합, ^ (합집합 00- 교집합)

    a -= set(range(0, 2)) # 0과 1은 소수가 아님

    #에리스토테네스의 체
    for i in range(2, int(max(a) ** 0.5) + 1): #max(a) ** 0.5 = math.sqrt(max(a))
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


print(solution('17'))