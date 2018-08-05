g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

print([next(g)])

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(100)

'''
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(100)
print(next(f))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)