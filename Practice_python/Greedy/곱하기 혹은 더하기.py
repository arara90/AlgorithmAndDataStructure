# 각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x'혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
# 일반적인 연산 방식과 달리 모든 연산을 왼쪽에서 부터 순서대로 이루어진다고 가정합니다.
# 02984로 만들 수 있는 가장 큰 수 는 ((0+2) * 9 * 8 * 4) = 576입니다
# 만들 수 있는 가장 큰수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# I Think
# 0 또는 1이면 + 나머지 2

data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)