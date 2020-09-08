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


##2
def solution(record):
    answer = []
    users = {}
    acts = []
    

    for i in record:
        data = i.split()
        acts.append(data[:2])
        
        if len(data) > 2:
            users[data[1]] = data[2]
        
    for act in acts:
        if(act[0]) == 'Enter':
            output  = f'{users[act[1]]}님이 들어왔습니다.'
        elif(act[0]) == 'Leave':
            output  = f'{users[act[1]]}님이 나갔습니다.'
        else:
            continue

        answer.append(output)
            
    return answer
# 테스트 1 〉	통과 (0.02ms, 9.53MB)
# 테스트 2 〉	통과 (0.02ms, 9.65MB)
# 테스트 3 〉	통과 (0.05ms, 9.53MB)
# 테스트 4 〉	통과 (0.06ms, 9.51MB)
# 테스트 5 〉	통과 (1.20ms, 9.83MB)
# 테스트 6 〉	통과 (1.14ms, 9.88MB)
# 테스트 7 〉	통과 (1.12ms, 9.79MB)
# 테스트 8 〉	통과 (1.17ms, 9.92MB)
# 테스트 9 〉	통과 (1.27ms, 9.88MB)
# 테스트 10 〉	통과 (1.25ms, 9.82MB)
# 테스트 11 〉	통과 (0.84ms, 9.68MB)
# 테스트 12 〉	통과 (0.84ms, 9.71MB)
# 테스트 13 〉	통과 (1.19ms, 9.85MB)
# 테스트 14 〉	통과 (1.21ms, 9.98MB)
# 테스트 15 〉	통과 (0.02ms, 9.45MB)
# 테스트 16 〉	통과 (0.02ms, 9.52MB)
# 테스트 17 〉	통과 (0.11ms, 9.61MB)
# 테스트 18 〉	통과 (0.11ms, 9.43MB)
# 테스트 19 〉	통과 (1.47ms, 9.92MB)
# 테스트 20 〉	통과 (1.17ms, 9.88MB)
# 테스트 21 〉	통과 (1.11ms, 9.78MB)
# 테스트 22 〉	통과 (1.19ms, 9.8MB)
# 테스트 23 〉	통과 (1.15ms, 9.88MB)
# 테스트 24 〉	통과 (1.10ms, 10MB)
# 테스트 25 〉	통과 (135.74ms, 57.5MB)
# 테스트 26 〉	통과 (141.65ms, 61.9MB)
# 테스트 27 〉	통과 (165.58ms, 64.7MB)
# 테스트 28 〉	통과 (138.19ms, 66.6MB)
# 테스트 29 〉	통과 (139.19ms, 66.2MB)
# 테스트 30 〉	통과 (112.47ms, 59.8MB)
# 테스트 31 〉	통과 (107.15ms, 62.7MB)
# 테스트 32 〉	통과 (89.41ms, 57.5MB)