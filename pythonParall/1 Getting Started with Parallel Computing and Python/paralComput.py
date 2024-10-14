import cProfile  # 导入cProfile库，用于性能分析
import multiprocessing  # 导入multiprocessing库，用于创建和管理进程
import os
import time  # 导入time库，用于模拟任务处理时间


def worker(q):
    """
    工作进程函数，处理队列中的任务

    参数：
        q (multiprocessing.JoinableQueue): 任务队列
    """
    while not q.empty():
        item = q.get()  # 获取任务
        print(f"Processing {item} in process {multiprocessing.current_process().pid}")
        time.sleep(1)  # 模拟任务处理时间
        q.task_done()  # 标记任务完成


def task():
    """
    任务函数，创建任务队列、工作进程，并等待所有任务完成
    """
    q = multiprocessing.JoinableQueue()  # 创建可加入队列
    # 填充队列
    for i in range(10):
        q.put(i)

    # 创建工作进程
    num_workers = multiprocessing.cpu_count()  # 获取CPU核心数
    processes = [multiprocessing.Process(target=worker, args=(q,)) for _ in range(num_workers)]

    # 启动工作进程
    for p in processes:
        p.start()

    # 等待所有任务完成
    q.join()


if __name__ == "__main__":
    print(f"CPU核心数:{os.cpu_count()}")  # f-string 运行时求值并在字符串中嵌入表达式
    # 使用cProfile模块进行性能分析
    profiler = cProfile.Profile()  # 创建性能分析器对象
    profiler.enable()  # 启动性能分析

    task()  # 执行任务

    profiler.disable()  # 停止性能分析
    profiler.print_stats()  # 打印性能分析结果
