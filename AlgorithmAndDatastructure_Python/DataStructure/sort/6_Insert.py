# 앞에다가 끼워넣는 삽입 정렬!
def insertSort(x):
    for size in range(1, len(x)):   # [2,1,6,7,3,5]
        val = x[size]               # 2
        i = size                    # i = 2부터 시작
        # 삽입할 위치 뒤에 있는애들 한칸씩 밀기
        while i > 0 and x[i-1] > val:   # i > 0 이고, i보다 밑에 있는 애가 현재 값(2) 보다 크다.
            x[i] = x[i-1]               # i 위치에 i-1의 값을 넣는다.
            i -= 1                      # i--
        x[i] = val                      # 삽입할 위치에 값 대입


x = [4,2,1,6,7,3,5]
print(x)
#print(x[1:4])
insertSort(x)
print(x)
