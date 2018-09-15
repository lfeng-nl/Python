#! python3


class A(object):
    def super_test(self):
        print('A')


class B(A):
    def super_test(self):
        print('B')


class C(B):
    def super_test(self):
        print('C')


class D(B):
    def super_test(self):
        print('D')


class E(C, D):
    def super_test(self):
        print('E')


class F(E):
    def super_test(self):
        super().super_test()
        print('F')


if __name__ == "__main__":

    # --> (<class '__main__.F'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    print(F.__mro__)

    f = F()
    # --> E F
    f.super_test()

    # 搜索的 MRO (<class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object')
    # --> E
    super(F, f).super_test()

    # 搜索的 MRO (<class '__main__.B'>, <class '__main__.A'>, <class 'object')
    # --> B
    super(D, f).super_test()