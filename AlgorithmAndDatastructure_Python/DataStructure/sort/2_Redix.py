## 기수 정렬 : 자릿수로 정렬 / queue 이용

## digit_number = (num / position) % 10
## 100의 자리를 기준으로 정렬하고자 한다면  :  2341 -( 100으로 나눈 몫 )-> 23 -( 10으로 나눈 나머지 )-> 3

# map?
# nums = list( map(lambda x :( int(x) / position )  % 10, li )) #[5, 0, 0, 6, 0, 9, 3, 7]

def radix(li):
    is_sorted = False
    position = 1

    while not is_sorted:
        print('position : ', position)
        is_sorted = True
        queue_list = [ list() for _ in range(10) ] # 리스트 내포 :queue_list = [ i for i in range(0,10) ]

        #  1. 현재 자릿수가 가진 숫자와 일치하는 queue_list 인덱스 위치에 append
        for num in li:
            # ex) num = 207, position=100이면 queue_list[2]에 207을 append
            digit_number = (int)(num / position) % 10
            queue_list[digit_number].append(num)

            # 2. while문 위한 조건 설정
            if is_sorted and digit_number > 0:          # 현재 100의 자릿수를 검사하고 있으면 100의 자릿수를 가지고 있는 애가 있는지 체크하고, 있으면 1000의 자릿수도 체크하게 된다.
                is_sorted = False                       # 107이 제일 큰 수라도 1000의 자릿수를 검사. 1000의 자릿수에서 digit_number가 모두 0이므로 is_sorted는 True로 유지하여 반복문 나감
                #print(num,digit_number, is_sorted)


        # 3. 원본 list에 재배치
        index = 0                       # index는 0
        for numbers in queue_list:      # 해당 자릿수에 들어있는 애들
            for num in numbers:
                li[index] = num
                index += 1

        # 4. 다음 자릿수 설정
        position *= 10
        print(li)


x = [5,107,106,20]
radix(x)



