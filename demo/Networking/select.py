import selectors
import socket

host = '127.0.0.1'
port = 8080
# 创建selector
sel = selectors.DefaultSelector()


def read(fileobj, mask):
    msg = fileobj.recv(1024)
    if msg:
        print('[server]', msg)
        if msg == b'exit':
            sel.unregister(fileobj)
            fileobj.close()


def accept(sock, mask):
    fileobj, addr = sock.accept()
    print('[server] accept', addr)
    # 注册连接生成的文件对象, 设置为非阻塞, 监听客户端发送内容
    fileobj.setblocking(False)
    sel.register(fileobj, selectors.EVENT_READ, data=read)


def main():

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen()
    # 将sock设置非阻塞
    sock.setblocking(False)
    # 使用selector监听可读(连接)事件 EVENT_READ/EVENT_WRITE
    sel.register(sock, selectors.EVENT_READ, data=accept)

    while True:
        events = sel.select(timeout=30)
        if not events:
            sel.close()
            print('[server] bye!')
            break
        # key: SelectorKey, namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])
        # mask: EVENT_READ/EVENT_WRITE
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


if __name__ == "__main__":
    main()
