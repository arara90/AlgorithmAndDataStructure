## 실패!! -> 계속작성하기

# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.


# 정렬 직접 작성해보기 (복습)

def marco(numbers):
    if 0 not in numbers:
        return -1
    else:
        nums = sorted(numbers, reverse=True)  # [2, 4, 4, 5, 5, 8]
        res = ''.join( map(str, nums))

        if int( res ) % 30 == 0 :
            return res

        else:
            nums = numbers
            tmp = 0

            for i in reversed(range( 0, len(numbers) - 1 )):
                #for j in
                    res = ''.join(map(str, nums))
                    if int(res) % 30 == 0:
                        return res
                    else:
                        return 0



numbers = list(map(int, list(input())))
print(marco(numbers))

