import multiprocessing
import threading
import time


def hander(arg):
    time.sleep(1)
    print('[%s] arg = %s' %
          (multiprocessing.current_process().pid, arg))
    return arg


def main():
    print('[main] pid =', multiprocessing.current_process().pid)
    with multiprocessing.Pool(processes=4) as pool:
        # map()调用多进程执行, 执行结果按调用顺序返回 [0,1,2,3,..9]
        print(pool.map(hander, range(10)))
        print('-' * 20)
        # imap() 返回生成器, 执行结果按调用顺序返回
        for i in pool.imap(hander, range(10)):
            print(i)
        print('-' * 20)
        # imap_unordered() imap的无序版本
        for i in pool.imap_unordered(hander, range(10, 20)):
            print(i)
        print('-' * 20)


if __name__ == "__main__":
    main()
