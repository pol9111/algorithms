from functools import reduce


def factorial(n, rst=1):
    for i in range(1, n):
        rst = rst*(i+1)
    print(rst)


factorial(5)


def factorial2(n):
    rst = n
    while n > 1:
        rst = rst * (n-1)
        n -= 1
    print(rst)


factorial2(5)


def factorial3(rst, n):
    return rst * n


rst = reduce(factorial3, [1,2,3,4,5])
print(rst)

