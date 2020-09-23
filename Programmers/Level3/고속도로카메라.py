# 카메라 적어도 한번
# 차량의 경로 routes [[-20,15], [-14,-5], [-18,-13], [-5,-3]]  
#[진입, 나간지점] -30,000 ~ 30,000
# 최소 몇개의 카메라?
# 차량 대수 1~10,000대 이하

def solution(routes=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]):
    answer = 0
    cars = [ i for i in range(len(routes))]

    #load 좌표 그리기용
    a = [y for x in routes for y in x]
    min_coord = abs(min(a))
    max_coord = abs(max(a))
    load = { i : [] for i in range(min_coord + max_coord) }

    
    for car, route  in enumerate(routes):
        for i in range(route[0]+min_coord, route[1]+min_coord):
            load[i].append(car)
        


    # leng = list(map(len, load.values()))
    res = load.sort(key=lambda e: len(e.value), reverse=True)

    print(res)
    # print(list(load.values()))
    
    
    return answer

    
solution()