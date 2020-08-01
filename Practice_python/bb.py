user_input = input()

orderArr = {
	'8' : 0,
	'5' : 1,
	'2' : 2,
	'4' : 3,
	'3' : 4,
	'7' : 5,
	'6' : 6,
	'1' : 7,
	'0' : 8,
	'9' : 9,
}

res = user_input.split(' ')
resdict= {}

for i in res:
	resdict.setdefault(orderArr[i], i)
	
sorteddict = sorted(resdict.items())


resList = []
for item in sorteddict:
	resList.append(item[1])

print(' '.join(resList))