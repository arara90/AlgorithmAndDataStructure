def num_generator():
    yield 1
    yield 2
    yield 3

for i in num_generator():
    print(i)


ng = num_generator()
a = next(ng)
print(a)

b = next(ng)
print(b)

c = next(ng)
print(c)


def Rgenerator():
    for i in range(10):
        return i

print(Rgenerator())


def Ygenerator():
    for i in range(10):
        yield i

print(Ygenerator())
g = Ygenerator()
print(dir(g))