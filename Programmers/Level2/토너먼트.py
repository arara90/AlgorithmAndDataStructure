def solution(n, a, b):
    # 초기화
    answer = 1
    team_a = a
    team_b = b

    while (True):
        # 현재 내 팀번호 구하기
        team_a = (team_a + 1) // 2
        team_b = (team_b + 1) // 2
        # print(team_a,team_b)
        if team_a == team_b:
            break

        answer += 1

    return answer