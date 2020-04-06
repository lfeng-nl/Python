# Python 代码风格

> [PEP8: Python 代码样式指导](https://www.python.org/dev/peps/pep-0008/);
>
> 代码格式检测工具:
>
> 代码格式化工具:

## 1.Python代码风格

### 1.命名风格

- 常量: 大写加下划线,`SQL_USER`
- 函数和方法: 小写加下划线`function_name`
- 私有元素: 双下环线开头;
- 参数: 小写加下划线;
- 类: 驼峰式命名;
- 模块和包: 都使用小写, 不带下划线;
- 命名指南:
  - 用`has`或`is`前缀命名布尔元素;
  - 用复数形式命名集合, 如`tables`;
  - 避免现有名称;

### 2.易错格式

- E128: 延续线下缩进视觉缩进, 该行字符太多时需要进行折叠:

  ```python
  a = test('abcdef', 'abcdef', 'abcdef', 'abcdef')
  # 括号内有内容, 缩进到括号
  a = test('abcdef',
           'abcdef', 'abcdef', 'abcdef')
  # 括号内无内容, 统一缩进
  a = test(
    'abcdef', 'abcdef', 'abcdef', 'abcdef')
  ```

- E711: `if info is None:`或`if not info is None`: 跟`None`的比较应用`is`;

## 2.格式检查工具

### 1.flake8 [doc](http://flake8.pycqa.org/en/latest/)

- 安装`pip install flake8`
- `flake8 file.py`
- 配置:

### 2.pycodestyle [doc](https://pycodestyle.readthedocs.io/en/latest/intro.html#id3)

- 根据 PEP8 样式检查 Python 代码是否符合;

- 安装`pip install pycodestyle`
- `pycodestyle file.py`

### 3.Pylint [doc](https://pylint.readthedocs.io/en/latest/)

- 安装`pip install pylint`
- [错误参考](http://pylint-messages.wikidot.com/all-messages)

## 3.代码格式化工具
