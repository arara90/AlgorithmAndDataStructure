#하나의 리스트에서 모든 조합 -> permutations, combinations
# 두개의 리스트의 모든 조함 -> product


#1.cartesian
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
# iterable3 = '1234'

iter = itertools.product(iterable1, iterable2)
print(*iter)
print([ ''.join(i) for i in itertools.product(iterable1, iterable2) ]) #['Ax', 'Ay', 'Bx', 'By', 'Cx', 'Cy', 'Dx', 'Dy']

#product(A, B)는 ((x,y) for x in A for y in B)

li = [ (x,y) for x in iterable1 for y in iterable2 ]
print(li) #[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]


#2.CombinationAndPermutations
#직접구현
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
print(list(map(''.join, itertools.combinations(pool,2))))




# 직접 구현
# https://blog.naver.com/kmh03214/221685090465
#조합
def combinations(arr,r):
    for i in range(len(arr)):  # 함수에서 지금할 일
        if r == 1:  # 종료조건
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1): # 다음에 할 일
                yield [arr[i]] + next



# 아래는 함수를 실행하기 위한 사용법입니다.
for combi in combinations([1,2,3,4,5],2):
    print(combi)


#중복조합
def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                yield [arr[i]] + next

#중복순열
def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr,r-1):
                yield [arr[i]] + next

