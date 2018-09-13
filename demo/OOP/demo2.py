#! python3
# 用于测试静态方法和类方法


class Test():
    a = 'abc'

    @staticmethod
    def static_method():
        print('static method')
        print(Test.a)

    @classmethod
    def class_method(cls):
        print('class method')
        print(cls.a)


if __name__ == '__main__':
    t = Test()
    t.static_method()
    t.class_method()
