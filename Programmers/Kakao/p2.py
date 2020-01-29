def solution(p):
    answer = pair_bracket(p)
    return answer


def pair_bracket(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. (종료조건)
    if len(p) == 0:
        return ''

    else:
        res = []
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
        #    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        u, v = divide(p)
        isPaired = check(u)

        if isPaired:
            #   3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
            #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
            res = u + pair_bracket(v)
            return res

        else:
            #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
            #   4-3. ')'를 다시 붙입니다.
            #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
            correctStr = "(" + pair_bracket(v) + ")"
            #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            u = list(u[1:-1])

            for i in range(0, len(u)):
                if u[i] == ")":
                    u[i] = "("
                else:
                    u[i] = ")"
            res = correctStr + ''.join(u)
            #   4-5. 생성된 문자열을 반환합니다.
            return res


def check(u):
    stack = []
    for i in range(0, len(u)):
        if u[i] == "(":
            stack.append(u[i])
        else:
            if len(stack) > 0:
                stack.pop(0)
            else:
                return False
    return True


def divide(p):
    # 갯수 기준으로 u,v나누기
    left = []
    right = []
    pivot = 0

    while pivot < len(p):
        if p[pivot] == "(":
            left.append(pivot)
        else:
            right.append(pivot)

        if len(left) == len(right):
            break
        pivot += 1

    return p[0:pivot + 1], p[pivot + 1:]