# 카메라 적어도 한번
# 차량의 경로 routes [[-20,15], [-14,-5], [-18,-13], [-5,-3]]  
#[진입, 나간지점] -30,000 ~ 30,000
# 최소 몇개의 카메라?
# 차량 대수 1~10,000대 이하


# print(list(remains.values()))
# print(remains.keys())
# print(remains.items())

#시간초과
def solution(routes=[[-20,15], [-14,-5], [-18,-13], [-5,-3]]):
    answer = 0

    #load 좌표 그리기
    routes = list(routes)
    a = [y for x in routes for y in x]
    min_coord = abs(min(a))
    max_coord = abs(max(a))

    #삽입삭제 쉽게 dict로 만들기
    remains = dict()
    cars = [ i for i in range(len(routes))]
    for car, route in zip(cars, routes):
        remains[car] = route

    def getMax(remains, load):
        maxlen = 0
        maxIdx = 0
        for car, route in remains.items():
            for i in range(route[0]+min_coord, route[1]+min_coord):
                load[i].append(car)
                maxlen, maxIdx = [len(load[i]), i] if maxlen < len(load[i]) else [maxlen, maxIdx]
        return maxIdx, load

    while(len(remains)>0):
        load = { i : [] for i in range(min_coord + max_coord) }
        # print(remains, load)
        idx,load = getMax(remains, load)
        for item in load[idx]:
            del remains[item]
        answer+=1

    return answer
    
print(solution())


#다른사람풀이
# 1. route를 오름차순 정렬
# 2. 앞쪽의 도착지점안에 뒤에거의 시작지점이 들어가면 겹치는 구간.
#    (  nextItem[0] <= maxCoord(이전에 검색했던 좌표들중에 가장 큰(먼?) 도착지점 값을 저장한 값 (preItem[1]) 면 )
# 3. 안겹치면  nextItem[0] > maxCoord 면 answer +=1 하면된다. 

def solution(routes):
    answer = 0
    routes.sort()

    standard = routes[0][1]
    routes.pop(0)
    answer+=1

    for item in routes:
        if item[0] <= standard:
            standard = min(item[1],standard)
        else:
            standard = item[1]
            answer+=1
    return answer


#허헐.. 너무 쉽고 빨라서 화가난다.