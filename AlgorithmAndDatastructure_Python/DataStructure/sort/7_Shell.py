# shell => shell단위? 삽입정렬 보완 / gap이용
# gap = int(len(li) / 2)

def Between(x, start, ranges):
    for target in range(start + ranges, len(x), ranges):
        val = x[target]
        i = target
        while i > start:
            if x[i-ranges] >val:
                x[i] = x[i-ranges]
            else:
                break
            i -= ranges
        x[i] = val

def shellSort(x):
    ranges=len(x)//2   # // 나눗셈의 몫
    while ranges > 0:
            for start in range(ranges):
                Between(x, start, ranges)
            ranges = ranges//2
    print(x)

x = [4,2,1,6,7,3,5]
shellSort(x)

