# Python测试和发布

## 1.单元测试

> "测试驱动开发 TDD"；单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例，在将来修改的时候，可以极大程度地保证该模块行为的正确性；

- 概念:

  - **测试脚手架 test fixture**: 开展测试所需的准备工作, 以及所有相关的清理操作;
    - 例如: 创建临时或代理的数据库, 目录, 再或者启动一个服务器进程;
    - `setUpClass(cls)`: 类方法, 运行单个类的测试之前调用的方法;
    - `tearDownClass(cls)`: 类方法, 单个类的测试运行后调用;
    - `setUp(self)`: 运行每个测试方法前都自动被调用;
    - `tearDown(self)`: 运行每个测试方法后自动被调用;
  - **测试用例**: 单元测试的基本模块, 一个独立的测试单元, 继承`TestCase`, 检查输入特定数据时的响应;
    - 可以定义若干名称以`test`开头的方法, 例如`test_xxx(self)`,
    - `TestCase`提供了一些方法来检测和断言故障;
      - `assertEqual(a, b)`: 相等
      - `assertNotEqual(a, b)`: 不等
      - `assertTrue(x)`: True
      - `assertFalse(x)`: False
      - `assertIsNone(x)`: x 为 None
      - `assertIsNotNone(x)`: x 不为 None
  - **测试套件** `TestSuite`: 测试用例或测试套件的集合;
    - `addTest(self, test)`: 添加一个测试用例到`TestSuite`; 批量添加`addTests(tests)`;
    - `run(result)`: 运行测试套件, 与遍历运行所有测试用例
  - **测试运行器**: 用于执行和输出测试结果的组件;
    - 命令行执行: `python -m unittest test_module`
    - `TextTestRunner`, 运行测试用例或测试套件, 结果以文本的形式打印;
  - 测试结果: `TestResult` 用于存储测试结果;

- 通常, 测试模块放置在项目的`tests`目录中;

  ```python
  # 导入单元测试模块
  import unittest

  #编写测试类，需要从 unittest.TestCase 继承
  class TestDict(unittest.TestCase):

      # 类方法, 所有测试用例调用前调用
      @classmethod
      def setUpClass(cls):
          pass

      # 类方法, 所有测试用例调用后调用
      @classmethod
      def tearDownClas(cls):
          pass

      # setUP, 可以用来完成前置工作, 每个测试用例前调用. 如果发生异常, 则测试方法不会被运行;
      def setUp(self):
          pass

      # tearDown, 测试结束后进行清理, 每个测试用例后调用. 如果setUp运行, 无论是否成功, 都会运行 tearDown
      def tearDown(self):
          pass

    # !!! 每一个测试方法必须以test开头，类似`test_xxx()`形式命名, 内部使用TestCase提供的断言方法, 例如assertEqual 进行测试
      def test_init(self):
          d = list(range(10))
          self.assertEqual(d[0], 0)
          self.assertEqual(d[2], 2)

    if **name** == '**main**': # main 使用 TextTestRunner 运行所有测试用例
      unittest.main()
  ```

## 2.pdb

- 启动pdb调试:

    - 代码中加入以下内容

    - ```python
        import pdb
        
        pdb.set_trace()
        ```

    - 当程序执行到`pdb.set_trace()`时, 会暂停, 等待用户输入.

- `pdb`命令简介 [参考](https://docs.python.org/zh-cn/3/library/pdb.html):

    - w: 打印堆栈回溯.
    - p expression: 在当前栈运行语句并打印.
    - n: 继续运行到当前函数的下一行.
    - r: 继续运行到函数返回.

## 3.打包发布
