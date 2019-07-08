# 최소 단위까지 (1개) 쪼갠 후, 합치면서 정렬
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:

        # 1. 둘 다 길이가 1 이상이면
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        # 2. left만 1이상
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]

        #3. right만 1이상
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result

x = [4,2,1,6,7,3,5]
print(merge_sort(x))