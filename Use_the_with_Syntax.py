# 在有两个相关的操作需要在一部分代码块前后分别执行的时候，可以使用 with 语法自动完成
# with 语法也叫做“上下文管理器”
# 在threading模块中，所有带有 acquire() 方法和 release() 方法的对象都可以使用上下文管理器。
# Lock
# RLock
# Condition
# Semaphore
import threading
import logging

# 使用logging模块进行输出
# 使用 % (threadName) 可以在每次输出的信息都加上线程的名字
# logging模块是线程安全的。这样可以区分出不同线程的输出
logging.basicConfig(
    level=logging.DEBUG,
    format="%(threadName)-10s %(message)s",
)


# 使用 with 语句可以简化锁的管理，避免忘记释放锁导致的死锁问题
def threading_with(statement):
    with statement:
        logging.debug("%s acquired via with" % statement)


def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug("%s acquired directly" % statement)
    finally:
        statement.release()


if __name__ == "__main__":
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore()
    threading_synchronization_list = [lock, rlock, condition, mutex]
    for synchronization in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(synchronization,))
        t2 = threading.Thread(target=threading_not_with, args=(synchronization,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
