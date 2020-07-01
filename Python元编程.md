# Python 元编程

## 1.元类

> **重要**:
>
> **类是`type`的实例, `__new__(cls)`创建实例, `__init__(self)`初始化实例;**
>
> **元类**: **继承于`type`**, 元类在普通类**定义(实例化)**的时候被调用, 通过重写`__new__`方法, 控制类的定义, 增加类属性的操作;
>
> 元类本身: 1.在定义类的时候, 调用该类的元类, 2.可以拦截类的创建, 3. 修改类的属性等操作, 4.返回修改之后的类;
>
> 主要用途: 创建 API, 例如 Django 的 ORM
>
> [参考](http://blog.jobbole.com/21351/)

- 用`class`语句创建的每个类都隐式地使用`type`作为其元类, 即类都是通过`type`构建的. `class`语句默认提供`class Test(metaclass=type):...`, _type 创建类_;
- `type(name, bases, dict)`:
  - `name` 类名, 并且会成为 [`__name__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#definition.__name__) 属性；
  - `bases` 基类, 元组类型; 并且会成为 [`__bases__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#class.__bases__) 属性；
  - `dict` 属性, 字典类型, 并且会被复制到一个标准字典成为 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 属性;

  ```python
  # 元类的创建
  # 元类一般以Metaclass结尾,表明是一个元类, 元类是创建类,必须从type类型派生；
  class ListMetaclass(type):
      # 重写 __new__ 方法, 在创建类时调用(注意,是创建类的时候);
      def __new__(cls, name, bases, attrs):
          attrs['add'] = lambda self, value: self.append(value)
          return super().__new__(cls, name, bases, attrs)

  # 传入metaclass时，Python解释器在创建Mylist时，要通过 ListMetaclass.__new__()来创建
  class Mylist(list, metaclass=ListMetaclass):
      pass
  # 或者使用装饰器
  @six.add_metaclass(ListMetaclass)
  class Mylist(object):
      pass
  ```

* `__class__`：一个实例所属的类；普通对象就是所属的类，普通类就是`type`或`元类`；
