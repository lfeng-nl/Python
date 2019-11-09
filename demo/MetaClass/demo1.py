# 定义元类 用于定义普通类, 拦截类的定义过程, 对类的定义实现控制
class MetaClassTest(type):
    def __new__(cls, name, bases, attrs):
        print('MetaClassTest __new__')
        attrs['test'] = 'test'
        return super().__new__(cls, name, bases, attrs)


class TestClass(metaclass=MetaClassTest):
    pass


if __name__ == "__main__":
    print(TestClass.test)
