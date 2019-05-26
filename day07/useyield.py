# -*- coding: utf-8 -*-
"""
yield 关键字学习
   File Name：     useyield
   Author :       jing
   Date：          2019-05-24
"""


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


def fib(n):
    """
    for n in range(1000):
        a=n
    这个时候range(1000)就默认生成一个含有1000个数的list了，所以很占内存
    :param n:
    :return:
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


def main2():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))
    print(g.send(7))


if __name__ == '__main__':
    main()


"""
说明：


"""
