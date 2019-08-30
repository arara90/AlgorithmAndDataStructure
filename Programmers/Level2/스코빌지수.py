## 정확정 : 38.1 / 38.1	효율성 : 0.0 / 11.9	총점 : 38.1 / 50.0

## level2 두번째 문제였는데, 첫번째 문제는 저번에 했던 끝말잇기라 10분 안에 풀었고
## 이 문제에서 거의 45분~50분 정도를 쓴 듯.

## heap을 쓰고 싶었는데 어떻게 코드를 짜야할지 바로 생각이 나지 않아서 시간을 많이 잡아먹을 것 같았다.
## 결국 그냥 일일이 비교하는 코드로 구현.. 정확도 테스트는 모두 통과했지만 효율성은 하나도 통과하지 못했다.

## 1. 현재 코드 시간 복잡도 계산해보기
## 2. heap으로 짜보기(우선순위큐)
## 3. 내가 생각한 heap이 맞는지 생각해보고, 최적 코드 만들어보기.

# def mixFood(list_s):
#     a = list_s.pop()
#     b = list_s.pop()
#     s = a + (b*2)
#     list_s.append(s)
#
#     i = len(list_s) - 1
#
#     while i > 0 :
#         parent = i - 1
#         if ( list_s[parent] < s ) :
#             ( list_s[parent], list_s[i] )  = ( list_s[i], list_s[parent] )
#             i = parent
#         else :
#             break
#     return list_s
#
# def solution(scoville, K):
#
#     # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
#     answer = 0
#     scoville = sorted(scoville, reverse = True)
#
#     # reverse했으니까 뒤에서부터 오는게 맞을듯
#     i = len(scoville) - 1
#     while i > 0:
#         if scoville[i] < K:
#             scoville = mixFood(scoville)
#             answer = answer + 1
#             i = len(scoville) - 1
#
#             if len(scoville) == 1:
#                 if scoville[0] < K:
#                     return -1
#                 else:
#                     return answer
#         else:
#             i = i-1
#
#     return answer
#
#
# print(solution([1, 2, 3, 9, 10, 12], 7))


## 간단하다.. heapq 라이브러리만 import하면 heap코드 모두 짜지 않아도되네!


##### 시간초과 !!.. 왜지?
def solution(scoville, K):
    import heapq
    # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
    answer = 0
    heap = []

    #1. heap에 담기
    while scoville:
        try:
            heapq.heappush(heap,scoville.pop(0))
        except IndexError:
            return -1

    #2. 제일 작은 값만 K와 검사하면 된다.
    while heap:
        a = heapq.heappop(heap)

        # 마지막 남은 값인 경우
        if not heap:
            if a < K:
                answer = -1
                break

        else:
            # 최소값만 비교해보기
            if a < K:
                # mix 점수 계산해서 heap에 push
                b = heapq.heappop(heap)
                s = a + b * 2
                heapq.heappush(heap, s)
                answer += 1

            # 최소값이 K보다 크므로, 모든 값이 K보다 크다.
            else :
                break


    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))



