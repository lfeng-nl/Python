# Python 面向对象

## 1.类定义

### 1.语法

- Python 中类的创建

  ```python
   class Student(object):
     # 类属性
     c1 = 'c1'
     # 成员函数
     def __init__(self, x,y..):
       self.m1 = x
       self.m2 = y
   ...

  ```

  - 成员命名规则:

    - `_xx`: 还是`_xx`, 只是表明这个成员不想被外部访问.
    - `__xx`: 最终变为 `_ClassName__xx`,用此表示是内部成员,同时控制外部对齐访问(有些书籍不建议此写法);
    - `__xx__`: 一般是作为系统保留的具有特殊作用的变量名, 用户属性禁止使用.

- 实例属性和类属性:

  - 实例(对象)属性: 通过`self`或实例对象直接绑定.

  - 类属性：直接在类定义中定义的属性，这种属性归类所有；

    ```python
    class Student(object):
      # __slots__ 属于类属性
      __slots__ = ('name')
      def __init__(self, name):
        # name 实例(对象)属性
        self.name = name
    ```

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

### 2.静态方法和类方法

- 普通方法: 第一个参数是`self`

- 类方法`classmethod`:

  - 用`@classmethod`修饰, 可以通过类和实例调用.
    - `@classonlymethod`: 只能通过类调用, 调用时会判断实例参数`instance`是否为`None`, 是则抛出异常;
  - `cls`: 相比于普通方法, 传递给它们的第一个参数是一个类对象`cls`而不是实例`self`, 因此可以在方法中调用类相关的属性和方法.
  - 常见用途: 定义备选构造方法.

- 静态方法`staticmethod`:

  - 用`@staticmethod`修饰, 没有`self`和`cls`参数.
  - 就是普通方法, 只是在类中定义, 而不是在模块中.
  - 不是必要选项.

- 区别点：(归根是两种方法传入参数不同) 1.两者都能通过实例或类调用，2.类方法第一个参数传入类，可以在方法内调用类属性；静态方法无传入参数，无法操作类属性，通常用于设置环境变量等操作；

  - 抽象方法: `@abc.abstractmethod`

- `__new__(cls, *args, **kwargs)`: 负责创建实例;

  - 需要调用父类的`__new__`方法, 生成实例, 并返回;

    ```python
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        # todo
        return self
    ```

## 2.属性管理

> Python 中, 数据的属性和处理数据的方法统称为属性.

### 1.属性限制

- `__slots__`:

  - 默认情况下, Python 在各个实例中名为`__dict__`的**字典**里存储实例属性.
  - `__slots__`一方面对实例属性做出限制, 另一方面, 避免了`__dict__`字典数据结构存在.
  - `__slots__`仅对自身类有效, 对于子类无效.
  - 建议: 仅为了节省内存时使用`__slots__`.

### 2.特殊属性

- `@property`:

  - 将一个方法转换为属性读取；
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

- `__getattr__`: 当对象查找属性失败时, 会调用`__getattr__`处理.
  - 非对象属性, 可以抛出`AttributeError`异常.
- `__setattr__`: 对属性赋值时调用.

- `__getattr__, __getattribute__, __getitem__`:

  - `__getattr__`: 当属性查询失败时, 调用;
  - `__getattribute__`: **所有属性调用入口**. 用`object.__getattribute__(self, attr)`避免循环调用;
  - `__getitem__`: 实现类似`obj['key']`的运算符重载;

- `dir(), getattr(), hasattr(), setattr(), vars()`:

  - `__dir__`: 方法, 不接受参数, 返回一个表示模块中可访问名称的字符串列表;
  - `__dict__`: 属性(dict类型), 用来存储实例的属性和值;
  - `dir`: 列出对象大多数属性
    - 默认使用`__dir__()`方法, 未提供时, 返回`__dict__`中的信息;
  - `vars()`: 返回对象的`__dict__`属性;
  - `getattr()`: 获取对象的指定属性的值, 不存在时返回异常或默认值;
  - `hasattr()`: 是否存在某种属性;
  - `setattr()`: 将指定属性置为新值;

## 3.继承

- MRO: Method Resolution Order 方法解析顺序(子类在前)
  - 类方法`mro()`: 返回方法解析顺序列表MRO.
  - `ClassType.__mro__`返回一个元组, 就是MRO;

- `super(cls, inst)`: [参考 1](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) [参考 2](http://funhacks.net/explore-python/Class/super.html)
  - 构造器, 实例化一个super对象, `inst`是`cls`的实例.
  - 工作方式: 1.获取`inst`的 MRO 列表; 2.在 MRO 中查找`cls`的`index`, 返回下一个类`MRO[index+1]`. 3.通过`__getattribute__`查找MRO, 返回属性.
  - 在方法中调用: `super().method(arg) 等同于 super(__class__, self).method(arg)`

- 混入(mixin)类是指继承两个或两个以上的类, 并将他们的特性混合在一起;
- python 应避免多重继承;

## 4.其他

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
