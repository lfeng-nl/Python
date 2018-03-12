#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

# 汉诺塔

def move(n, a, b, c):
    if n == 1:
        print('%s --> %s'%(a,c))
    elif n == 2:
        print('%s --> %s'%(a,b))
        print('%s --> %s'%(a,c))
        print('%s --> %s'%(b,c))
    else:
        move(n-1, a, c, b)
        print('%s --> %s'%(a,c))
        move(n-1, b, a, c)

if __name__ == '__main__':
    n = int(input('请输入第一根柱子上盘子的数目：'))
    move(n,'A', 'B', 'C')