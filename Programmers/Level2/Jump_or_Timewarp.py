# 1. 한글자 이상?
# 2. 이전에 말한 단어?
# 3. 앞사람의 끝단어와 일치?

def get_res(num,n):
    return [ num % n + 1, num //n + 1 ] 

def solution(n, words):
    answer = [0,0]

    for i in range(1, len(words)):
        if len(words[i]) < 1 :
            answer = get_res(i, n)
            break
        elif words[i] in words[0:i-1]:
            answer = get_res(i, n)
            break
        elif words[i][0] != words[i-1][-1]:
            answer = get_res(i, n)
            break

    return answer