# -*- coding: utf-8 -*-
#利用切片，实现一个trim(), 去除字符串首位的空格

def trim(s):
    begin = 0
    end = len(s)
    for x in s:
        if x == ' ':
            begin += 1
        else:
            break
    for x in reversed(range(end)):
        if s[x] == ' ':
            end -= 1
        else:
            break
    
    s = s[begin:end]
    return s

if __name__ == "__main__":
    s = input("请输入一个字符串：")
    print('您输入的字符串为：|%s|' % s)
    print("|%s|" % trim(s))