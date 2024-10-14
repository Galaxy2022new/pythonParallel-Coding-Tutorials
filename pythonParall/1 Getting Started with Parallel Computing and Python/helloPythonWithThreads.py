# 为了支持多线程的Python程序，CPython使用了一个叫做全局解释器锁（Global Interpreter Lock， GIL）的技术。
# 这意味着同一时间只有一个线程可以执行Python代码；
# 执行某一个线程一小段时间之后，Python会自动切换到下一个线程。
# GIL并没有完全解决线程安全的问题，如果多个线程试图使用共享数据，还是可能导致未确定的行为

from threading import Thread
from time import sleep


# To create a thread in Python you'll want to make your class work as a thread.
class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python CookBook!!\n"

    # this method prints only the message
    def print_message(self):
        print(self.message)

    # 打印 10 次消息
    def run(self):
        print("Thread Starting\n")
        x = 0
        while x < 10:
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ending\n")


# start the main process
print("Process Started")

# 创建实例
hello_python = CookBook()

# print the message...starting the thread
hello_python.start()

print("Process Ended")
