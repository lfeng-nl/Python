#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

def product(x, *n):
    if len(n) == 0:
        return x
    for m in n:
        x = x * m
    return x


if __name__ == "__main__":
    print(product(5))
    print(product(5,2))
    print(product(5,2,3))
    print(product(5,2,3,4))
    print(product(5,2,3,4,5))