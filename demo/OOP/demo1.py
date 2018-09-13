#! python3
# 用于测试 __getattribut__, __getattr__, __get__, __getitem__ 

class C(object):
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        print('args', args)
        print('kwargs', kwargs)
        print('-' * 10)
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("__getattr__() is called ")
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def __setitem__(self, name, value):
        print('__setitem__ is called')
        self.__dict__[name] = value

    def __getitem__(self, name):
        print('__getitem__ is called')
        return self.__dict__[name]


class C2(object):
    c = C()


if __name__ == '__main__':
    c = C()
    c.a
    c.b
    c['name'] = 'test'
    c['name']

    c2 = C2()
    c2.c.a