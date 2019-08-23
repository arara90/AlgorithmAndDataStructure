

def solution(arr):
    answer = 0
    b = arr[0]

    for i in range(1, len(arr)):
        a = arr[i]
        n, m = a, b

        while (b > 0)
            # 조건1 a>b 여야한다. 아닌 경우 a,b swap.
            if a < b:
                (a, b) = (b, a)
            else:
                if a % b == 0:
                    break
                else:
                    (a, b) = (b, a % b)

    return answer