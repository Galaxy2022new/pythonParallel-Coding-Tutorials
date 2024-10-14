# Python3.2带来了 concurrent.futures 模块，这个模块具有线程池和进程池、
# 管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能
# 此模块由以下部分组成：
# concurrent.futures.Executor: 这是一个虚拟基类，提供了异步执行的方法。
# submit(function, argument): 调度函数（可调用的对象）的执行，将 argument 作为参数传入。
# map(function, argument): 将 argument 作为参数执行函数，以 异步 的方式。
# shutdown(Wait=True): 发出让执行者释放所有资源的信号。
# concurrent.futures.Future: 其中包括函数的异步执行。Future对象是submit任务（即带有参数的functions）到executor的实例。

# current.Futures 模块提供了两种 Executor 的子类，各自独立操作一个线程池和一个进程池。这两个子类分别是：
# concurrent.futures.ThreadPoolExecutor(max_workers)
# concurrent.futures.ProcessPoolExecutor(max_workers)
# max_workers 参数表示最多有多少个worker并行执行任务s

import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    result_item = count(x)
    return result_item


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i * number


if __name__ == "__main__":
    # 顺序执行
    start_time = time.time()
    for item in number_list:
        print(evaluate_item(item))
    print("Sequential execution in " + str(time.time() - start_time), "seconds")
    # 线程池并行
    start_time_1 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Thread pool execution in " + str(time.time() - start_time_1), "seconds")
    # 进程池
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Process pool execution in " + str(time.time() - start_time_2), "seconds")
# 和 ThreadPoolExecutor 不同的是， ProcessPoolExecutor 使用了多核处理的模块，
# 让我们可以不受GIL的限制，大大缩短执行时间
