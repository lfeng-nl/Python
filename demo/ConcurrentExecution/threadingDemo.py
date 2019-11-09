import threading
import time


def hander(sleep_time):
    print('[%s] sleep %s' % (threading.current_thread(), sleep_time))
    time.sleep(sleep_time)
    print('[%s] ok' % threading.current_thread())


def main():
    # 初始化线程对象, daemon守护线程,主线程退出, 不需要等待子线程
    t1 = threading.Thread(target=hander, name='t1', args=(4,), daemon=True)
    t2 = threading.Thread(target=hander, name='t2', args=(3,), daemon=True)
    t3 = threading.Thread(target=hander, name='t3', args=(10,))

    t1.start()
    t2.start()
    t3.start()
    print('[main] join')
    t3.join()
    print('[main] ok!')


if __name__ == "__main__":
    main()
