import multiprocessing
import time


def hander(sleep_time):
    print('[%s] sleep %s' % (multiprocessing.current_process().pid, sleep_time))
    time.sleep(sleep_time)
    print('[%s] ok!' % multiprocessing.current_process().pid)


def main():
    # 初始化子进程, 使用方式和相关接口类似Thread
    p1 = multiprocessing.Process(
        target=hander, name='p1', args=(20, ), daemon=True)
    print('[main %s] start process' % multiprocessing.current_process().pid)
    p1.start()
    time.sleep(2)
    print('[main] ok!')


if __name__ == "__main__":
    main()
