# -*- coding: utf-8 -*-

# 利用闭包实现计数器


def createCounter():
    r = 0

    def f():
        nonlocal r
        r += 1
        return r

    return f


if __name__ == '__main__':
    f1 = createCounter()
    f2 = createCounter()
    print("f1: %d"%f1())
    print("f2: %d"%f2())
    print("f1: %d"%f1())
    print("f1: %d"%f1())
    print("f1: %d"%f1())
    print("f2: %d"%f2())
    print("f2: %d"%f2())
    print("f2: %d"%f2())
    print("f2: %d"%f2())
    print("f2: %d"%f2())