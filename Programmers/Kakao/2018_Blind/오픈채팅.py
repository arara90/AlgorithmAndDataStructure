def solution(record):
    answer = []
    members = {}

    for item in record:
        act = item.split()
        # act[0] = Enter or Leave or Change, act[1] = uid, act[2] = nickname
        if act[0] != 'Leave':
            members[act[1]] = act[2]

    for item in record:
        act = item.split()
        if act[0] == 'Enter':
            answer.append(members[act[1]] + "님이 들어왔습니다.")
        elif act[0] == 'Leave':
            answer.append(members[act[1]] + "님이 나갔습니다.")
    return answer


if __name__ == "main":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))