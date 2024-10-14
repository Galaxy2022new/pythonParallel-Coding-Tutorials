import cProfile  # 导入 cProfile 模块，用于性能分析
import concurrent.futures  # 导入 concurrent.futures 模块，用于并发执行任务
import numpy as np  # 导入 numpy 库，用于数组操作
import os  # 导入 os 模块，用于获取 CPU 核心数
import time  # 导入 time 模块，用于计时


# 下面我们将使用一个稍复杂的程序来演示这些内容。这个程序将使用 Python 的并行计算库来计算一个大数组中的平方和。

# 这个函数会计算一个数组的平方和。
def calculate_squares(arr):
    """
    计算数组的平方和

    参数：
        arr (numpy.ndarray): 输入的数组

    返回：
        float: 平方和
    """
    return np.sum(np.square(arr))


# 这个函数会将一个大数组分割成小块，并使用多个进程并行计算每块的平方和，然后将结果合并。
def parallel_square_sum(arr, num_splits):
    """
    并行计算数组的平方和

    参数：
        arr (numpy.ndarray): 输入的数组
        num_splits (int): 分割的块数

    返回：
        float: 平方和
    """
    # 分割数组
    splits = np.array_split(arr, num_splits)

    square_sum = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(calculate_squares, splits):
            square_sum += result

    return square_sum


def main():
    # 创建一个大数组
    arr = np.random.rand(10 ** 7)

    # 首先，我们计算串行版本的运行时间。
    start_time = time.time()
    square_sum = calculate_squares(arr)
    end_time = time.time()
    serial_time = end_time - start_time
    print(f"Serial time: {serial_time} seconds")

    # 然后，我们计算并行版本的运行时间。我们将数组分割成与 CPU 核心数相同的块。
    start_time = time.time()
    square_sum_parallel = parallel_square_sum(arr, os.cpu_count())
    end_time = time.time()
    parallel_time = end_time - start_time
    print(f"Parallel time: {parallel_time} seconds")

    # 验证结果是否正确
    assert np.isclose(square_sum, square_sum_parallel), "Results do not match!"

    # 计算并行效率和加速比
    parallel_efficiency = serial_time / (parallel_time * os.cpu_count())
    speedup = serial_time / parallel_time
    print(f"Parallel efficiency: {parallel_efficiency}")
    print(f"Speedup: {speedup}")

    # 使用 cProfile 分析并行版本的性能
    profiler = cProfile.Profile()
    profiler.enable()
    square_sum_parallel = parallel_square_sum(arr, os.cpu_count())
    profiler.disable()
    profiler.print_stats(sort='time')


if __name__ == "__main__":
    main()
