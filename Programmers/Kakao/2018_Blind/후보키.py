# DFS ? 단방향으로 풀어보기
# 이미 시간 초과 / 끼기긱.

# 1. 각각의 컬럼이 갖을 수 있는 조합 정보
# ex) 1->2, 1->3, 1->4 / 2->3, 2->4, 3->4, 4


# def solution(relation):
#     answer = 0
#     row_size = len(relation)
#     col_size = len(relation[0])
#     map_edges=[]
#     edges = []
#     print('col_size', col_size)


#     # i+1
#     for i in range(0, col_size):
#         print('i: ', i)
#         map_edges.append(  [ _ for _ in range(0, col_size-i) ] )
#     print(map_edges)

#     for i in range(0,col_size):
#         for j in range(0, len(map_edges[i])):
#             print([i,j])
#             for k in range(0, i+1 ):
#                 map_edges[i][j] = k

#         print(f' ----------- {i} ----------- ')
#     print(map_edges)




#################################################################
import itertools


def solution(relation):
    answer = list()
    k = 1 << len(relation[0]) #columns의 모든 조합만들기
    
    for i in range(1, k):
        key=set()
        if next((x for x in answer if i & x ==x ), None ) : continue
           
        for row_idx in range(len(relation)):
            can_visit = lambda x: i & ( 1 << x ) # 현재 col이 원하는 조합에 해당되는가
            key.add(''.join(
                [item for col, item in enumerate(relation[row_idx]) if can_visit(col)]))
        if (len(key) == len(relation)):
            answer.append(i)
    return len(answer)



relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(solution(relation))

## 라이브러리 사용
# from itertools import chain, combinations

# def get_all_unique_subset(iterable):
#     s = list(iterable)
#     return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

# def solution_lib(relation):
#     unique_list = get_all_unique_subset(relation)
#     unique_list = sorted(unique_list, key=lambda  x: len(x))

#     #부분집합 중에서 최소성을 만족하는 부분집함(열의 쌍) 구하기
#     answer_list = []
#     for subset in unique_list:
#         subset = set(subset)
#         check = True
#         for j in answer_list:
#             if j.issubset(subset):
#                 check=False
            
#         if check == True:
#             answer_list.append(subset)
        
#         return len(answer_list)

# relation = [["100","ryan","music","2"],
#             ["200","apeach","math","2"],
#             ["300","tube","computer","3"],
#             ["400","con","computer","4"],
#             ["500","muzi","music","3"],
#             ["600","apeach","music","2"]]

# print(solution_lib(relation))