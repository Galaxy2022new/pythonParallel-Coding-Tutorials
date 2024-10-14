# 想让只有拿到锁的线程才能释放该锁
# 需要在类外面保证线程安全，又要在类内使用同样方法
# 1. 谁拿到谁释放。如果线程A拿到锁，线程B无法释放这个锁，只有A可以释放；
# 2. 同一线程可以多次拿到该锁，即可以acquire多次；
# 3. acquire多少次就必须release多少次，只有最后一次release才能改变RLock的状态为unlocked

import threading
import time


class Box(object):
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


# 这两个函数在不同的线程中运行，并调用盒子的方法
def adder(box, items):
    while items > 0:
        print("adding 1 items in the box")
        box.add()
        time.sleep(1)
        items -= 1


def remover(box, items):
    while items > 0:
        print("removing 1 items in the box")
        box.remove()
        time.sleep(1)
        items -= 1


if __name__ == '__main__':
    items = 5
    print("putting %s items in the box" % items)
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("%s items added to the box" % items)
