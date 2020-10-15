# 특정원소가 속한 집합 찾기 (x는 노드번호)
def find_parent(parent, x):
    # 루트 노드 찾을 때까지 재귀
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')

for i in range(1, v+1):
    print(find_parent(parent, i), end='')


print()


# 부모테이블내용 출력
print('부모테이블 : ', end='')
for i in range(1, v+1):
    print(parent[i], end='')

# #문제점
# 합집합(union)연산
# 이 편향되게 이루어지는 경우 찾기(Find)함수가 비효율적으로 동작
# 최악의 경우에는 찾기(Find)함수가 모든 노드를 다 확인하게 되어 시간 복잡도 O(V)

# union(4,5),union(3,4),union(2,3),union(1,2)
# 1<-2<-3<-4<-5 의경우
# 1,2,3,4,5
# 1,1,2,3,4


# 경로압축기법
# -> 찾기 함수를 재귀함수로 호출한 뒤에 부모 테이블 값을 바로 갱신

def find_parent2(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 1,2,3,4,5
# 1,1,1,1,1 <=요런식으로 된다.
