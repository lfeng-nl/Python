# -*- coding: utf-8 -*-

# normalize:将用户输入的不规范英文名字，变为首字母大写，其他字母小写
# prod: 接收一个list并求积

def normalize(name):
    return name[0].upper() + name[1:].lower()

def prod(L):
    r = 1
    for x in L:
        r *= x
    return r


if __name__ == '__main__':
    L1 = ['hello', 'HELLO', 'hEllO']
    L2 = list(map(normalize, L1))
    print(L1)
    print(L2)

    L3 = [[1,2,3], [2,3,1], [2,4,5]]
    print(list(map(prod, L3)))
