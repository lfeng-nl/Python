# Python 网络编程

## 1.WSGI

> 定义一种接口, `application(environ, start_response)`, 当请求时, 服务器生成环境信息, 调用指定的接口 app, 传入`environ`环境信息, `start_response`回调, 并接受返回值
>
> [参考](https://www.python.org/dev/peps/pep-3333/)

- 应用程序必须接受两个位置参数;

- `environ`: 字典对象, 包含 CGI 风格的环境变量, 还必须包含 WSGI 所需的环境变量;

  - `CGI`风格, 大写, 例如,`REQUEST_METHOD`: 请求方式, `"GET", "POST"`;
  - `WSGI`风格, 小写, 例如`wsgi.version`, wsgi 版本;

- `start_response(status, response_headers, exc_info=None)`: 接受两个参数的可调用对象,

  - status: 格式必须为`"200 ok", "999 Message here"`;
  - `response_headers`: 格式为`[(head, head_value)]`, list 类型, 元素为包含头部和信息的 tupe,
  - `exc_info`: 异常信息;
  - 以上信息会写入 data

- `application`必须返回一个可迭代对象, 产生 0 个或多个`byts`类型,

- python 中的简单测试

  ```python
  from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
  def application(environ, start_response):
      status = '200 OK'
      response_headers = [('Content-type', 'text/plain')]
      start_response(status, response_headers)
      return [b'hello']

  # 配置服务器
  server = WSGIServer(('0.0.0.0', 80), WSGIRequestHandler)
  server.set_app(application)
  # 启动服务器, 当监听到连接时, 通过`_handle_request_noblock()`处理, 该函数内部通过 一系列调用, 最后会实例化RequestHandlerClass, ReqestHandlerClass初始化时会执行handle方法 对于WSGI, WSGIRequsestHandler().handle();
  server.server_forever()

    def handle(self):
        handler = ServerHandler(
            self.rfile, self.wfile, self.get_stderr(), self.get_environ())
        handler.request_handler = self      # backpointer for logging
        handler.run(self.server.get_app())

    def run(self, application):
        # 生成environ环境信息
        self.setup_environ()
        # 调用指定的application, 传入回调函数 start_response
        self.result = application(self.environ, self.start_response)
        # 处理返回,响应请求
        self.finish_response()

    # 接受status, headers, 将数据写入data (HTTTP协议的头部信息)
    def start_response(sefl, starus, handers):
    pass
  ```
