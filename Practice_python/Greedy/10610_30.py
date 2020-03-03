# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
#
# 입력 : N을 입력받는다. N는 최대 10^5개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.
#       -> 첫 배열크기 지정할 때 중요한 조건
# 출력 : 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.


# 접근방법
# 1. 정수론 : 30의 배수가 되는 조건은? N의 배수가 되려면 소인수 분해해서 나타난 수들을 포함해야한다.
# 2. 하지만 이 문제의 경우 30을 3*10으로 나누어서 생각하자
#   1) 10으로 최소 1번이상 나눌수 있음 (0이 무조건 있어야함)
#   2) 모든 자릿수들의 합이 3의 배수
# 3. 위 조건이 만족하면 내림차순으로 정렬해준다.

## The first Trial : 31144KB	292ms
## 수정해볼것 :
### 1. 정렬직접작성
### 2. output 과정 예) list -> 문자열 -> 숫자 간단히?
def marco(numbers):
    # 조건 1번
    if 0 not in numbers:
        return -1

    else:
        sum = 0
        for item in numbers:
            sum += item

        if sum % 3 == 0:
            numbers = sorted(numbers, reverse=True )

            # list -> 문자열 -> 숫자
            res = ''
            for i in numbers:
                res = res + str(i)

            res = int(res)
            return res

        else :
            return -1


# input은 문자열로 들어온다. int로 바꿔줘야한다.
numbers = list(map(int, list(input())))

# 리스트 -> 문자열 -> 숫자로
print(marco(numbers))


