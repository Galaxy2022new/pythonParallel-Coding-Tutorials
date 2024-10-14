# 信号量是一个内部数据，用于标明当前的共享资源可以有多少并发读取
# 每当线程想要读取关联了信号量的共享资源时，必须调用 acquire() ，此操作减少信号量的内部变量,
#   如果此变量的值非负，那么分配该资源的权限。如果是负值，那么线程被挂起，直到有其他的线程释放资源。
# 当线程不再需要该共享资源，必须通过 release() 释放。这样，信号量的内部变量增加，
#   在信号量等待队列中排在最前面的线程会拿到共享资源的权限。

import threading
import time
import random

semaphore = threading.Semaphore(0)  # 同步两个或多个线程

def consumer():
    print('Consumer is waiting')
    semaphore.acquire()  # 如果信号量的计数器到了0，就会阻塞 acquire() 方法，直到得到另一个线程的通知。如果信号量的计数器大于0，就会对这个值-1然后分配资源
    print("Consumer notify : consumed item number %s " % item)

def producer():
    global item
    time.sleep(10)
    item = random.randint(1, 1000)
    print("producer notify : produced item number %s" % item)
    semaphore.release()  # 可以提高计数器然后通知其他的线程

if __name__ == '__main__':
    for i in range(0, 5):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("program end")