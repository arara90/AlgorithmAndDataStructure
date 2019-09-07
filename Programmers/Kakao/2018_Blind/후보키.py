# DFS ? 단방향으로 풀어보기
# 이미 시간 초과 / 끼기긱.

# 1. 각각의 컬럼이 갖을 수 있는 조합 정보
# ex) 1->2, 1->3, 1->4 / 2->3, 2->4, 3->4, 4





def solution(relation):
    answer = 0
    row_size = len(relation)
    col_size = len(relation[0])
    map_edges=[]
    edges = []
    print('col_size', col_size)


    # i+1
    for i in range(0, col_size):
        print('i: ', i)
        map_edges.append(  [ _ for _ in range(0, col_size-i) ] )
    print(map_edges)

    for i in range(0,col_size):
        for j in range(0, len(map_edges[i])):
            print([i,j])
            for k in range(0, i+1 ):
                map_edges[i][j] = k






        print(f' ----------- {i} ----------- ')

    print(map_edges)





# 1. 시작점 설정
# 2. 다음 노드 가져오기


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

a = solution(relation)