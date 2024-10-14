# 同一进程的多个不同的线程可以共享相同的资源。相比而言，进程之间不会共享资源。
# 每一个线程基本上包含3个元素：程序计数器，寄存器和栈
# 线程的状态大体上可以分为ready,running,blocked
# 线程模块的主要组件如下：
#   线程对象
#   Lock对象
#   RLock对象
#   信号对象
#   条件对象
#   事件对象
#
# class threading.Thread(group=None,
#                        target=None,
#                        name=None,
#                        args=(), # 元组 tuple
#                        kwargs={}) # 字典 dict
# 上面的代码中：
#   group: 一般设置为 None ，这是为以后的一些特性预留的
#   target: 当线程启动的时候要执行的函数
#   name: 线程的名字，默认会分配一个唯一名字 Thread-N
#   args: 传递给 target 的参数，要使用tuple类型
#   kwargs: 同上，使用字典类型dict

import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


threads = []

for i in range(5):
    # 将当前循环中的 i 传递给 function 目标函数
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()  # t 线程执行结束，主线程才会继续执行）
