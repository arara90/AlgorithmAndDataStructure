def solution(N, stages):
    # N : 스테이지의 수 (최대 500)
    # stage : 유저가 머믈고 있는 곳(index)과 유저수 (value)
    stage = [0 for i in range(0, N + 1)]
    num_user = len(stages)  # 전체유저수

    # 1. 각 스테이지별로 유저 넣기
    for i in stages:
        stage[i - 1] += 1

    # 2. 실패율 구하기 - 초기화 작업
    total_user = num_user
    fail_rates = {}

    # 3. 실패율 구하기 - 각 스테이지 별 실패율
    for i in range(0, N):
        if total_user == 0:
            fail_rate = 0
        else:
            fail_rate = stage[i] / total_user
            total_user = total_user - stage[i]  # 낙오자 제외!

        fail_rates[i + 1] = fail_rate

    # 이는 result라는 딕셔너리 자료형을 value값 내림차순 기준으로 key를 정렬하는 역할을 한다.
    answer = sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)
    return answer



if __name__ == "main":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]	# [3,4,2,1,5]
    print(solution(N, stages))