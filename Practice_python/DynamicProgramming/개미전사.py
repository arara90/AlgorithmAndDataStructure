# 동빈나 이코테 https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6

# 개미 전사는 부족한 식량을 충당하고지 메뚜기 마을의 식량창고를 몰래 공겨가려고 합니다. 메뚜기 마을에는 여러개의
# 식량창고가 있는데 식량창고는 일직선으로 이어져 있습니다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며, 개매전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정입니다.
# 이때, 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있습니다.
# 따라가 정찰병에서 들키지 않고 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야합니다.
# (연속적으로 고를 수 없다)

# 예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정합니다.
# [1,3,1,5]
# 이 때, 게미 전사는 두 번째 식량창고와 네번째 식량 창고를 선택했을때 최댓값인 8개의 식량을 빼앗을 수 있습니다.
# 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오

# 조건
# 풀이시간 30분 | 시간제한 1초 | 메모리 128MB
# 첫째줄: 3 <= N(식량창고의 개수) <= 100
# 둘째줄: 저장된 식량 개수 0 <= K <= 1000
# 출력 : 얻을 수 있는 식량의 최댓값

# 경우의 수
# 1000
# 0100
# 0010
# 0001
# 1010
# 1001
# 0101
# 0000

# 창고0까지만 있다면 1
# 창고1까지만 있다면 -> 3
# 창고2까지만 있다면 -> 3
# 창고3까지만 있다면 -> 8

# dp(i-2) + i(현재식량창고) 나 dp(i-1) 중에 큰 값을 선택한다.
# 즉 a(i) = max(a(i-1), a(i-2)+k)

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

# bottomup
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])
