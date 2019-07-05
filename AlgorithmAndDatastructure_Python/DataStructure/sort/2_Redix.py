def radix(li):
    is_sorted = False
    position = -1

    while not is_sorted:
        is_sorted = True
        queue_list = [ list() for _ in range(10) ] # 0 ~ 1000000000 자릿수

        for num in li:
            digit_number = (int)(num/position) % 10 # 자릿수
            queue_list[digit_number].append(num) # 현재 자릿수에 해당하는 숫자 큐에 저장

            # 처음 for문에 들어왔고, 아직 계산해야할 자릿수가 남았으면 is_sorted=False
            if is_sorted and digit_number > 0 :
                is_sorted = False


            index = 0                       # index는 0
            for numbers in queue_list:      # 해당 자릿수에 들어있는 애들
                for num in numbers:
                    li[index] = num
                    index += 1
            position *= 10  # 다음 자릿수로 이동





x = [5,20,80,6,100,9,3,7]
radix(x)
print(x)
