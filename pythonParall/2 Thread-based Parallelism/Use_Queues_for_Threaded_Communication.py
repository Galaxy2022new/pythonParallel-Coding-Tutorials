# 队列可以将资源的使用通过单线程进行完全控制，并且允许使用更加整洁和可读性更高的设计模式
# Queue
# put(): 往queue中放一个item
# get(): 从queue删除一个item，并返回删除的这个item
# task_done(): 每次item被处理的时候需要调用这个方法
# join(): 所有item都被处理之前一直阻塞

from threading import Thread
from queue import Queue
import time
import random


class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(
                "Producer notify: item N° %d appended to queue by %s"
                % (item, self.name)
            )
            time.sleep(1)


class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print("Consumer notify : %d popped from queue by %s" % (item, self.name))
            self.queue.task_done()


if __name__ == "__main__":
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t4 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
