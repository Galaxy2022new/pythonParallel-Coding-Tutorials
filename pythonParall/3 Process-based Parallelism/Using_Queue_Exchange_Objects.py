# Multiprocessing库有两个Communication Channel可以交换对象：
# 队列(queue)
# 管道（pipe）

import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(1, 256)
            self.queue.put(item)
            print("Process Producer : item %d appended to queue %s" % (item, self.name))
            time.sleep(1)
            print("The size of queue is %s" % self.queue.qsize())


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("The queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(
                    "Process Consumer : item %d popped from by %s \n"
                    % (item, self.name)
                )
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

# 队列还有一个 JoinableQueue 子类，它有以下两个额外的方法：
#
# task_done(): 此方法意味着之前入队的一个任务已经完成，比如， get() 方法从队列取回item之后调用。所以此方法只能被队列的消费者调用。
# join(): 此方法将进程阻塞，直到队列中的item全部被取出并执行。