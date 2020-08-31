# 문제 설명
# 다음을 만족하는 함수, solution을 완성해주세요.

# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [ [1,2,3], [4,5,6], [7,8,9] ]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

# 제한 조건
# mylist의 원소의 길이는 모두 같습니다.
# mylist의 길이는 mylist[0]의 길이와 같습니다.
# 각 리스트의 길이는 100 이하인 자연수입니다.

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))

print(list(zip(*mylist))) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)] 

# zip - 튜플 Returns an iterator of tuples, 시퀀스나 이터러블의 i번째 요소를 포함하는 tuple 반환
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

# example1 - 여러개의 iterable 동시 순회
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k ) #493 124 66 305

# example2 - 두 리스트 합쳐서 딕셔너리로 만들기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
print(answer)

