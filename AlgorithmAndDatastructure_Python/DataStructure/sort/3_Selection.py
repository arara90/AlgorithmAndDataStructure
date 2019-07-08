# 선택정렬
def change(x,i,j):
    x[i], x[j] = x[j], x[i]
    print(x)


## 큰거부터
def selectrionSort_max(x):
    for size in reversed(range(len(x))): # 반대로 검색 0,1,2,3,4 -> 4,3,2,1,0
        max_i = 0

        # 제일 큰 거 찾기!
        for i in range(1,1+size): # 1,2,3,4 -> 1,2,3 -> 1,2 -> 1
            if x[i]>x[max_i]:
                max_i = i

        # 제일 큰 것은 맨 뒤로!
        change(x, max_i, size)


## 작은거부터
def selectrionSort_min(x):

    for index in range(len(x)):  # 검색 0,1,2,3,4
        min_i = index
        # 제일 작은 거 찾기!
        for i in range(index, len(x)):
            if x[i] < x[min_i]:
                min_i = i
        change(x,min_i,index)


x = [4,2,1,6,7,3,5]
selectrionSort_min(x)
print('dafggsg')
selectrionSort_max(x)

