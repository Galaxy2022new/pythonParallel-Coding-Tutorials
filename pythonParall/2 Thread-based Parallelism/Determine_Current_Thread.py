import threading
import time

# 因为 Python 的 print() 函数本质上不是原子操作，线程之间的 print 调用可能会出现竞争（race condition）。
# 换句话说，多个线程可能在控制台输出的过程中互相干扰，导致输出错乱，尤其是在线程中使用 print() 的时候。
# 确保每个线程的输出独立，并且换行正常，可以使用线程锁（threading.Lock）来防止多个线程同时写入控制台。
lock = threading.Lock()


# 确保每个线程的输出独立，并且换行正常，可以使用线程锁（threading.Lock）来防止多个线程同时写入控制台。


def first_function():
    with lock:
        print(threading.current_thread().name, str('is Starting'))
    time.sleep(2)
    with lock:
        print(threading.current_thread().name, str('is Finished'))
    return


def second_function():
    with lock:
        print(threading.current_thread().name, str('is Starting'))
    time.sleep(2)
    with lock:
        print(threading.current_thread().name, str('is Finished'))
    return


def third_function():
    with lock:
        print(threading.current_thread().name, str('is Starting'))
    time.sleep(2)
    with lock:
        print(threading.current_thread().name, str('is Finished'))
    return


if __name__ == "__main__":
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(target=third_function)  # 默认命名：Thread-1 (third_function)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
