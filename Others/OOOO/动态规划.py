from timeit import Timer


def memo(func):
    cache = {}
    def wrap(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrap


fib = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)

@memo
def fib1(n):
    global fib
    return fib(n)


@memo
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


@memo
def fib3(n):
    if n <= 2:
        return n
    return fib(n-1) + fib(n-2)


# rst = fib3(20)
# print(rst)


t1 = Timer("fib1(20)", "from __main__ import fib1, memo")
print("fib1:",t1.timeit(number=1000), "seconds")
t2 = Timer("fib2(20)", "from __main__ import fib2")
print("fib2:",t2.timeit(number=1000), "seconds")
t3 = Timer("fib3(20)", "from __main__ import fib3, memo")
print("fib2:",t3.timeit(number=1000), "seconds")