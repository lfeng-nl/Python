# -*- coding: utf-8 -*-
# 杨辉三角生成器

def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[n]+l[n+1] for n in range(len(l)-1)] + [1]

if __name__ == '__main__':
    s = triangles()
    for x in range(10):
        print(next(s))