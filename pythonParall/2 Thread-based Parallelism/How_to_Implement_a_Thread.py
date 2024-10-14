# 定义一个 Thread 类的子类
# 重写 __init__(self [,args]) 方法，可以添加额外的参数
# 最后，需要重写 run(self, [,args]) 方法来实现线程要做的事情
# 最后，需要重写 run(self, [,args]) 方法来实现线程要做的事情
import threading
import time
import _thread

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name + "...")
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "...")


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting Main Thread")
