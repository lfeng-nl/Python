# Python 面向对象

> 一切类(包括`type, object`)都是`type`的实例;
>
> 所有类(包括`type`)都继承于`object`;
>
> python 一切皆对象:
>
> 1.  **`type`是自身的实例**, `type`继承于`object`, 所以 type is a object;
> 2.  所有类都是`type`的实例, type 继承于`object`, 所以 class is a object;
> 3.  所有类都继承于`object`, 所以对象 is a object;

## 1.基本语法

- Python 中类的创建：

  - ```python
    class Student(object):
      # 类属性
      c1 = 'c1'
      # 成员函数
      def __init__(self, x,y..):
        self.m1 = x
        self.m2 = y
    ...

    ```

  - 成员命名规则：

    - `_xx`：还是`_xx`，只是表明这个成员不想被外部访问；
    - `__xx`：最终变为 `_ClassName__xx`，用此表示是内部成员，同时控制外部对齐访问；
    - `__xx__` ：还是 `__xx__`，一般是作为系统保留的具有特殊作用的变量名；

- 实例属性和类属性：

  - 实例(对象)属性：给实例对象绑定属性的方法是通过实例变量，或者通过`self`变量；

  - 类属性：直接在`class`中定义属性，这种属性归类所有；

    ```python
    class Student(object):
      	def __init__(self, name):
          	self.name = name			# 实例对象属性
        xxx = '302'					    # 类属性
    ```

  - 创建类的实例后，可以给 实例绑定任何属性和方法，绑定的属性和方法只跟这个实例对象有关，跟类和其他实例无关；

- 关于对象的一些函数:

  - 使用`isinstance()`判断对象是否为某种类型的实例；
  - 使用`dir()`获得一个对象的所有属性和方法；
  - 使用`hasattr()`判断一个对象是否具有某种属性或方法；
  - 使用`getattr(object, name[, default])`获取一个对象的属性;
  - 使用`setattr(object, name, value)`设置一个对象的属性;

- `type()` ：1.查看一个类型或变量类型，2.创建一个新类型；通过`type()`函数创建的类和直接写 class 是完全一样的，因为 Python 解释器遇到 class 定义时，仅仅是扫描一下 class 定义的语法，然后调用`type()`函数创建出 class。

  ```python
  # 要创建一个class类，type()函数以此传入3个参数：
  # 1.calss的名称
  # 2.继承的父类集合，（元组，所以，当只有一个时写法为‘（xxx,）’）
  # 3.calss的方法名称 和 函数绑定

  def fn(self, name="world"):
      print('Hello, %s.'%name)

  Hello = type("Hello", (object,), dict(hello=fn))
  ```

- **普通方法, 静态方法和类方法**

  - 普通方法: 第一个参数是`self`
  - 静态方法：嵌套在一个类中，用`@staticmethod`修饰, 没有`self`和`cls`参数, 几乎相当于普通函数, 只是与该类有关联;
  - 类方法：相比于普通方法, 传递给它们的第一个参数是一个类对象而不是实例`cls`, 因此可以在方法中调用类相关的属性和方法；用`@classmethod`修饰, 可以通过类和实例调用；`@classonlymethod`: 只能通过类调用, 调用时会判断实例参数`instance`是否为`None`, 是则抛出异常;
  - 区别点：(归根是两种方法传入参数不同) 1.两者都能通过实例或类调用，2.类方法第一个参数传入类，可以在方法内调用类属性；静态方法无传入参数，无法操作类属性，通常用于设置环境变量等操作；
  - 抽象方法: `@abc.abstractmethod`

* `__new__(cls, *args, **kwargs)`: 负责创建实例;

  - 需要调用父类的`__new__`方法, 生成实例, 并返回;

    ```python
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        # todo
        return self
    ```

## 2.属性管理

- `@property`:

  - 将一个方法转换为属性调用；

  - `@property` 还会创建另一个装饰器`@属性名.setter`；负责把`xxx`方法变成属性赋值，不定义`setter`方法，则该属性就为只读的；

    ```python
    class A(object):

        # get方法
        @property
        def name(self):
            return self._name

        # set方法
        @name.setter
        def name(self, name):
            self._name = name

        # 属性删除
        @name.deleter
        def name(self):
            pass
    ```

- `__getattr__, __getattribute__, __getitem__`:

  - `__getitem__`: 实现类似`obj['key']`的运算符重载;
  - `__getattr__`: 实现当属性查询失败时, 自动处理;
  - `__getattribute__`: 所有属性调用入口. 用`object.__getattribute__(self, attr)`避免循环调用;

- `dir(), getattr(), hasattr(), setattr(), vars()`:

  - `dir`: 列出对象大多数属性, 默认使用`__dir__()`方法, 未提供时, 返回`__dict__`中的信息;
  - `vars()`: 返回对象的`__dict__`属性;
    - `__dir__()`: 不接受参数, 返回一个表示模块中可访问名称的字符串列表;
    - `__dict__`: 用来存储**对象**属性的一个字典, 例如在`__init__()`中定义的, 通过实例字节附加上的;
  - `getattr()`: 从对象总获取指定属性的值, 不存在时返回异常或默认值;
  - `hasattr()`: 是否存在某种属性;
  - `setattr()`: 将指定属性置为新值;

## 3.Python 如何实现继承

> `ClassType.__mro__`返回一个元组, 就是一个简单的所有基类的线性顺序表; 称为: MRO( **Method Resolution Order** 方法解析列表)列表(子类在前);

- `super(cls, inst)`: [参考 1](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) [参考 2](http://funhacks.net/explore-python/Class/super.html)
  - 1. 获取`inst`的 MRO 列表; 2.在 MRO 中查找`cls`的`index`, 返回下一个类`MRO[index+1]`,
  - 在方法中调用: `super().method(arg) 等同于 super(__class__, self).method(arg)`
- 混入(mixin)类是指继承两个或两个以上的类, 并将他们的特性混合在一起;
- python 应避免多重继承;

## 4.特殊方法(魔术方法)

> 类中有很多类似`__xxx__`之类的函数，可以作为钩子，实现特殊的功能, 称为魔术方法；[参考](https://docs.python.org/zh-cn/3/reference/datamodel.html#basic-customization)

- 基础
  - `__init__(self,...)`：构造函数，对象被创建时调用；
  - `__new__(cls, ...)`: 用于创建实例并返回, 在`__init__`前被调用, 重写时需要显示调用并返回父类`__new__()`方法;
  - `__del__(self)`：在对象被销毁时调用；
  - `__str__(self)`：返回一个字符串，在实例化对象被`print()`或`str()`调用时调用；
  - `__repr__(self)`: 返回一个字符串, 在`repr()`中调用,**交互式终端中用于提示** , `__str__`不存在时替代`__str__`功能;
  - `__call__()`: 可调用;
- 运算符重载
  - `__getitem__(self, key)` ：使用`x[key]`索引操作符的时候调用;
  - `__setitem__(self, key, value)`：使用`x[key]`索引赋值;
  - `__call__` ：实例化对象本身可以做为一个方法，直接对实例进行调用；
  - `__add__(self, other)`：重载运算符`+`；此外还有`__radd__, __iadd__`
  - `__lt__(), __le__(), __eq__(), __ne__(), __gt__(), __ge__()...`
- 迭代器
  - `__iter__(self)` ：如果一个类想被用于`for...in`循环，就必须实现一个`__iter__()`方法；该方法返回一个迭代对象，然后，Python 的`for`循环就会不断调用该迭代对象的`__next__()` 方法拿到循环的下一个值；
    - 可迭代对象就是含有`__iter__()`方法的对象;
  - `__next__`: 返回容器下一个元素;
- 字符串
  - `__repr__`: 使用`repr`获取对象的字符串形式时, 会调用`__repr__`方法, 例如终端里打印一个对象;
  - `__str__`: 使用`str()`函数时被调用, 当`__str__`未实现时, 会调用`__repr__`方法;
- 数值转换
  - `__abs__, __bool__, ...`
- 属性访问控制
  - `__slots__`: 显式声明数据成员；
  - `__getattr__(self, name)`: 定义当用户试图获取一个不存在的属性的行为;
  - `__getattribute__(self, name)`: 属性访问拦截器, 访问类的属性时控制被访问时的行为, **注意避免循环调用**;
  - `__setattr__(self, name, value)`: 定义属性被赋值时的行为;
  - `__dict__`: 对象的属性字典;
  - `__dir__()`: 在`dir()`被调用时调用
    - `dir()`:返回包含属性的列表, 如果对象提供`__dir__()`方法，直接使用， 除此使用`dir()`逻辑, 包含实例的属性，类的属性和递归基类的属性;
- 上下文管理器
  - `__enter__(self)`进入上下文管理器调用;
  - `__exit__(self, exc_type, exc_value, trace)`退出上下文管理器调用;
    - `exc_type, exc_value, trace`: 可用于异常处理；
- 其他
  - `__module__`: 当前对象的类型所在模块;
  - `__class__`: 当前对象的类;
  - `__hash__`：应该同`__eq__()`一同定义， 表示可哈希；
  - `__bases__`: 由基类所组成的元组;

## 6.其他

- 通过槽限制属性: 通过`__slots__`变量，通过给该变量赋值一个元组，来规定允许绑定的属性名称和方法名称；_只对自身类起作用，对通过继承的子类不起作用_；

  - ```python
    class A(object):
        # 只允许存在名为name、age的属性或方法
        __slots__ = ('name', 'age')
        pass
    ```

- 枚举类：通过`Enum`类定义的类型；`value`属性则是自动赋给成员的`int`变量；

  ```python
  from enum import Enum
  Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  Month.Jan.value
  >> 1

  # 还可以精确的控制枚举类型
  from enum import Enum, unique

  @unique     #帮助检查保证没有重复值
  class Weekday(Enum):
      Sun = 0 # Sun的value被设定为0
      Mon = 1
      Tue = 2
      Wed = 3
      Thu = 4
      Fri = 5
      Sat = 6
  ```

  - `@unique` 装饰器可以帮助我们检查保证没有重复值;
