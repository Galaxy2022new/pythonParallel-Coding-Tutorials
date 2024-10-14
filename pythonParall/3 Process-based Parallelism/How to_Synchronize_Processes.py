# Barrier: 将程序分成几个阶段，适用于有些进程必须在某些特定进程之后执行。
# 处于障碍（Barrier）之后的代码不能同处于障碍之前的代码并行。
# 其余方法跟线程一样

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == "__main__":
    synchronizer = Barrier(2)  # 声明一个 Barrier，等待两个进程达到同步点
    serializer = Lock()  # 声明一个锁，用于同步输出
    # test_with_barrier 函数调用了barrier的 wait() 方法
    Process(
        name="p1 - test_with_barrier",
        target=test_with_barrier,
        args=(synchronizer, serializer),
    ).start()
    # Barrier(2) 创建了一个屏障，要求两个进程必须都调用 wait() 方法到达屏障，同步点才会触发
    Process(
        name="p2 - test_with_barrier",
        target=test_with_barrier,
        args=(synchronizer, serializer),
    ).start()
    Process(name="p3 - test_without_barrier", target=test_without_barrier).start()
    Process(name="p4 - test_without_barrier", target=test_without_barrier).start()
