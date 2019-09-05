# DFS ? 단방향으로 풀어보기
# 이미 시간 초과 / 끼기긱.

# 1. 각각의 컬럼이 갖을 수 있는 조합 정보
# ex) 1->2, 1->3, 1->4 / 2->3, 2->4, 3->4, 4





def solution(relation):
    answer = 0
    col_size = len(relation[0])
    graph = []

    for i in range(0, col_size):
        graph[i] = [ col_num for col_num in range( i+1, col_size )  ]


    print(graph)

    return answer


graph =[col_num for col_num in range( 1, 5) ]
print(graph)
# a = solution([ [1,2,3,4,5]])