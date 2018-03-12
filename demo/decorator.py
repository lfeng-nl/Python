# -*- coding: utf-8 -*-

# 装饰器，作用于任何函数之上，并打印该函数的执行时间；

import datetime
import functools


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(datetime.datetime.now())
        return func(*args, **kw)

    return wrapper


if __name__ == '__main__':

    @metric
    def test(x):
        return 2*x

    print(test(2))