def solution(d, budget):
    # d = 신청금액, budget = 예산
    # 최대로 지원해줄 수 있는 부서
    answer = 0
    total = 0
    for i in sorted(d):
        if budget - i < 0 :
            break
        else:
            budget = budget - i
            answer += 1

    return answer

print(solution([1,2,3,4,5,6], 8))