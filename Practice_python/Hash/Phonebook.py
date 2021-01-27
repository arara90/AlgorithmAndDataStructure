
def solution(phone_book):
    answer = True
    phone_book.sort()
    dc={}
    
    for item in phone_book:
        tmpNum=''
        dc[item] = 1
        for i in item:
            tmpNum += i
            if tmpNum != item and tmpNum in dc:
                return False
    

    return answer

print(solution([119, 97674223, 1195524421]))