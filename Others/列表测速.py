

from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l.append(i)


def test2():
    l = []
    for i in range(1000):
        l += [i]


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


def test5():
    l = []
    for i in range(1000):
        l.extend([i])

t1 = Timer("test1()", "from __main__ import test1")
print("append:  ",t1.timeit(number=10000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("+:       ",t2.timeit(number=10000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("i for i: ",t3.timeit(number=10000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list():  ",t4.timeit(number=10000), "seconds")
t5 = Timer("test5()", "from __main__ import test5")
print("extend:  ",t5.timeit(number=10000), "seconds")

