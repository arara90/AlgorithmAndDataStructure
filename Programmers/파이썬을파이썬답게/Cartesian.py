#cartesian
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
# iterable3 = '1234'

iter = itertools.product(iterable1, iterable2)
print(*iter)
print([ ''.join(i) for i in itertools.product(iterable1, iterable2) ]) #['Ax', 'Ay', 'Bx', 'By', 'Cx', 'Cy', 'Dx', 'Dy']

#product(A, B)는 ((x,y) for x in A for y in B)

li = [ (x,y) for x in iterable1 for y in iterable2 ]
print(li) #[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]