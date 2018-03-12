# -*- coding: utf-8 -*-
# 找到给定列表的最大值和最小值

def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for x in L:
        if max < x:
            max  = x
        elif min > x:
            min = x
    return min, max

if __name__ == '__main__':
    print(findMinAndMax([1,2,3,4,5]))