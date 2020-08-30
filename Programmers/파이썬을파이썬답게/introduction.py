#나쁜예 => C, java에 가까움
def Badsolution(mylist):
    answer=[]
    for i in mylist:
        answer.append(len(i))
    return answer

def solution(mylist):
    return list(map(len, mylist))



print(solution([[1,2], [1], [1,2,3]]))

