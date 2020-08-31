import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
flag = True

for number in numbers:
    multiplied *= number
    print('multiplied', multiplied)
    print('math.sqrt(multiplied)', math.sqrt(multiplied))
    print('int(math.sqrt(multiplied))', int(math.sqrt(multiplied)))
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        flag = False
        print('found')
        break

if flag:
    print('not found')


## in python
import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')