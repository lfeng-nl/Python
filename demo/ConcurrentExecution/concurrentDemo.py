from concurrent import futures
import multiprocessing
import threading
import time


def hander(arg):
    print('[%s] arg = %s' %
          (multiprocessing.current_process().pid, arg))
    time.sleep(10)
    return arg


def main():
    # 可以使用 ThreadPoolExecutor 或 ProcessPoolExecutor, 指定线程池的最大数量
    with futures.ThreadPoolExecutor(max_workers=10, thread_name_prefix='future') as executor:
        # 调用map(), 
        for i in executor.map(hander, range(10)):
            print(i)


if __name__ == "__main__":
    main()
