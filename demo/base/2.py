#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


#接收三个参数，返回一元二次方程的解

import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        print("参数类型错误")
        return None
    if not isinstance(b, (int, float)):
        print("参数类型错误")
        return None
    if not isinstance(c, (int, float)):
        print("参数类型错误")
        return None
    
    d = b**2 - 4*a*c

    if d<0:
        print('方程无实根')
        return None
    elif d == 0:
        print('方程仅有一个解')
        return(-b/2/a)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print('方程有两个解')
        return(x1,x2)


if __name__ == '__main__':
    print('请出入三个系数：')
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
    print("方程为：%fx^2+%dx+%d"%(a,b,c))
    x = quadratic(a,b,c)
    print(x)