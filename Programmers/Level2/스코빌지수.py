## 정확정 : 38.1 / 38.1	효율성 : 0.0 / 11.9	총점 : 38.1 / 50.0

## level2 두번째 문제였는데, 첫번째 문제는 저번에 했던 끝말잇기라 10분 안에 풀었고
## 이 문제에서 거의 45분~50분 정도를 쓴 듯.

## heap을 쓰고 싶었는데 어떻게 코드를 짜야할지 바로 생각이 나지 않아서 시간을 많이 잡아먹을 것 같았다.
## 결국 그냥 일일이 비교하는 코드로 구현.. 정확도 테스트는 모두 통과했지만 효율성은 하나도 통과하지 못했다.

## 1. 현재 코드 시간 복잡도 계산해보기
## 2. heap으로 짜보기(우선순위큐)
## 3. 내가 생각한 heap이 맞는지 생각해보고, 최적 코드 만들어보기.

def mixFood(list_s):
    a = list_s.pop()
    b = list_s.pop()

    s = a + (b*2)
    list_s.append(s)

    i = len(list_s) - 1

    while i > 0 :
        parent = i - 1
        if ( list_s[parent] < s ) :
            ( list_s[parent], list_s[i] )  = ( list_s[i], list_s[parent] )
            i = parent
        else :
            break
    return list_s


def solution(scoville, K):

    # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
    answer = 0
    scoville = sorted(scoville, reverse = True)

    i = 0

    # K검사
    while i < len(scoville) :
        if ( scoville[i] < K ):
            scoville = mixFood(scoville)
            answer = answer + 1

            if len(scoville) == 1 :
                if scoville[0] < K:
                    return -1
                else :
                    return answer

        else :
            i+=1

    return answer