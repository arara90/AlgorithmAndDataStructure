# 효율성 0 점...ㅠ.ㅠ .. 다 구해서 그럴까?


def solution(n):
    global tmp_list
    tmp_list = [0 for _ in range(0, n)]
    tmp_list[0:2] = [0, 1, 1]

    for i in range(0, n+1):
        if i < 3:
            #print('i<3', i, tmp_list[i] )
            pass

        else :
            if (i % 2 == 0):
                tmp_list[i] = min(tmp_list[int(i/2)], tmp_list[i-1]+1)
            else:
                tmp_list[i] = tmp_list[i-1]+1

            #print('i>3', i, tmp_list[i])

    ans = tmp_list[n]
    print(tmp_list)
    return ans

print(solution(5000))