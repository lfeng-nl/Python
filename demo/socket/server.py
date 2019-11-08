import socket
import threading
BACKLOG = 5

host = '127.0.0.1'
port = 8080


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(BACKLOG)
    s.setblocking
    print('[server] begin...')
    while True:
        s_fd, addr = s.accept()
        print('[server] connect form ', addr)
        t = threading.Thread(target=hander, args=(s_fd, addr), daemon=True)
        t.start()


def hander(s_fd, addr):

    while True:
        msg = s_fd.recv(1024).decode('utf-8')
        if msg == 'exit':
            print('[server] bye', addr)
            s_fd.close()
            break
        print('[server: %s] %s' % (addr, msg))


if __name__ == "__main__":
    main()
