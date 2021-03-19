# stack, queue 문제 항목들을 stack이나 queue를 사용하는 것 보다는
# 로직을 차근차근 풀어내는게 더 어려운것 같다.

# 결국 로직이 꼬여서 제한시간(30분)내로 푸는 것에는 실패했다.
# 다른 사람의 풀이를 참고해서 완성했다.

# 원래 total값을 따로 계산하지 않고 매번 sum(q)를 사용하는 로직이었는데,
# 결국 한번씩 순회하면서 total을 구하기 때문에 list가 길어지면 성능이 급격하게 저하된다.
# (n ^ 2)

# 참고
# https: // docs.python.org/3/library/functions.html  # sum
# Sums start and the items of an iterable from left to right and returns the total.


# 따라서, sum하지 않고 + /-로 변수에 담아두면 매번 list의 값들을 계산하지 않아도 되기 때문에
# 속도를 개선할수 있다. (n)


# def solution(bridge_length, weight, truck_weights):
#     q = [0]*bridge_length
#     sec = 0
#     while q:
#         sec += 1
#         q.pop(0)
#         if truck_weights:
#             if sum(q)+truck_weights[0] <= weight:
#                 q.append(truck_weights.pop(0))
#             else:
#                 q.append(0)
#     return sec


def solution(bridge_length, weight, truck_weights):
    q = [0]*bridge_length
    sec = 0
    total = 0  # total weight : bridge 위에 있는 트럭들의 총 무게
    truck = 0

    while q:
        sec += 1
        truck = q.pop(0)
        total -= truck

        if truck_weights:
            if total+truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                q.append(truck)
                total += truck

            else:
                q.append(0)
    return sec


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()


### 실제 비교 ###

# 테스트 1 〉	통과 (12.73ms, 10.3MB)            테스트 1 〉	통과 (1.05ms, 10.3MB)
# 테스트 2 〉	통과 (1522.65ms, 10.3MB)          테스트 2 〉	통과 (48.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)             테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (334.66ms, 10.3MB)           테스트 4 〉	통과 (10.14ms, 10.3MB)
# 테스트 5 〉	통과 (9693.98ms, 10.3MB)          테스트 5 〉	통과 (292.72ms, 10.2MB)
# 테스트 6 〉	통과 (1664.87ms, 10.2MB)          테스트 6 〉	통과 (41.65ms, 10.2MB)
# 테스트 7 〉	통과 (7.19ms, 10.3MB)             테스트 7 〉	통과 (0.75ms, 10.3MB)
# 테스트 8 〉	통과 (0.34ms, 10.1MB)             테스트 8 〉	통과 (0.13ms, 10.2MB)
# 테스트 9 〉	통과 (5.98ms, 10.3MB)             테스트 9 〉	통과 (2.95ms, 10.3MB)
# 테스트 10 〉	통과 (0.43ms, 10.3MB)           테스트 10 〉	통과 (0.18ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)           테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.50ms, 10.2MB)           테스트 12 〉	통과 (0.24ms, 10.2MB)
# 테스트 13 〉	통과 (3.93ms, 10.2MB)           테스트 13 〉	통과 (1.04ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)           테스트 14 〉	통과 (0.02ms, 10.2MB)
