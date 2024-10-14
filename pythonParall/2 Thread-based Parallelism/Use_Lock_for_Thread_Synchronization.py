import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


# 需要使用资源的时候，调用 acquire() 拿到锁（如果锁暂时不可用，会一直等待直到拿到），最后调用 release():
# 有两个方法来操作锁： acquire() 和 release()
#   如果状态是unlocked， 可以调用 acquire() 将状态改为locked
#   如果状态是locked， acquire() 会被block直到另一线程调用 release() 释放锁
#   如果状态是unlocked， 调用 release() 将导致 RuntimError 异常
#   如果状态是locked， 可以调用 release() 将状态改为unlocked
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


def increment_with_no_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_with_no_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_with_no_lock)
    t4 = threading.Thread(target=decrement_with_no_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("the value of shared_resource_with_lock is {}".format(shared_resource_with_lock))
    print("the value of shared_resource_with_no_lock is {}".format(shared_resource_with_no_lock))
