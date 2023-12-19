# b = lambda a:a**2

# print(b(4))

def myfunc(n):
    return lambda x:x*n

doubler = myfunc(2)
tripler = myfunc(3)
quadrupler = myfunc(4)

print(doubler(10))
print(tripler(10))
print(quadrupler(10))
