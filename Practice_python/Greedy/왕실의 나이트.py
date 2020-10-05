# 8*8 좌표 평면의 왕실 정원. 정원의 특정한 한 칸에 나이트가 서 있습니다.
# 나이트는 말을 타고 있기 때문에 이동 할 때는 L자 형태로만 이동할 수 있으며, 정원 밖으로 나갈 수 없습니다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
#     1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
#     2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

# 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력/
# 행 위치는 1~8, 열 위치는 a~h

# ex) c2에 있을 때, 이동 가능한 경우의 수는 6가지 입니다.

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향
steps = [(2, 1),(2,-1),(-2, 1),(-2, -1),(1, 2),(-1, 2),(1, -2),(-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    #이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <=8:
        result += 1

print(result)