import socket

host = '127.0.0.1'
port = 8080


def main():
    s = socket.socket()
    s.connect((host, port))
    print('[client] connect server!')
    while True:
        msg = input('请输入:')
        s.send(msg.encode('utf-8'))
        if msg == 'exit':
            s.close()
            break


if __name__ == "__main__":
    main()
