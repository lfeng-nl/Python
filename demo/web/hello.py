def application(environ, start_response):
    start_response('200 0k', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!<img src="./test.jpg" /></h1>']