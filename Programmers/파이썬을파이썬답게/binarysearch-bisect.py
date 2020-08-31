#직접구현
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3)) #2 -> 3이 있는 index

#in python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3)) #3 ->  insertion point출력, 즉 3 다음에 있는 2+1 인덱스를 출ㄹ력
#Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a


#주의할점
# https://programmers.co.kr/questions/7270
# 기존 Binary Search는 찾고자 하는 key 값이 발견되지 않으면 -1을 리턴하지만
# bisect 모듈들은 key값이 없으면 해당 key값이 들어갈 위치를 반환합니다.

import bisect
def b_s(ary,key):
    i= bisect.bisect(ary,key)
    return i-1 if ary[i-1]==key else -1


class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return '({},{})'.format(self.x, self.y)

point = Coord(1,2)
print(point)