# 这是一个使用Python的threading库来演示数据竞争条件和同步（通过锁）的例子。
import threading

# 全局计数器变量
counter = 0


def increment(lock):
    global counter
    for _ in range(100000):
        with lock:
            # 如果去掉 with lock: 最后的输出结果小于200000，这是因为两个线程可能同时读取、修改和写回 counter 变量，造成了数据的丢失
            counter += 1


# 创建一个锁的对象
lock = threading.Lock()

# 创建两个线程，都指向同一个函数
thread1 = threading.Thread(target=increment, args=(lock,))
thread2 = threading.Thread(target=increment, args=(lock,))

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print(counter)

# 在 increment_counter 函数中，每次修改全局变量 counter 时，都会先获得锁，然后才进行修改，修改完后释放锁。
# 这样可以保证在任何时刻，只有一个线程能够访问和修改 counter，从而避免了数据竞态条件。
