# Python 的函数 map(aFunction, aSequence) 将在序列的每一个元素上调用传入的函数，并将结果以 list 的形式返回
# map 示例，内置的 map 函数比手动写 for 循环的性能更高。
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # def multiplyFor2(x):return x*2
# # print(list(map(multiplyFor2,items)))
# print(list(map(lambda x: x**2, items)))  # 将 lambda 函数（不用绑定变量名的匿名函数）当做参数传给 map 函数
import functools

# SCOOP 模块提供了多个 map 函数可以将异步计算任务下发到多个计算节点：
#
# futures.map(func, iterables, kargs) : 此函数返回一个生成器，可以按照输入的顺序遍历结果。可以说是内置 map 函数的一个并行执行版本。
# futures.map_as_completed(func, iterables, kargs) : 每当有结果出现时，就立刻 yield 出来。
# futures.scoop.futures.mapReduce(mapFunc, reductionOp, iterables, kargs) : map 函数执行过后可以通过此函数执行 reduction 函数。返回结果是一个元素。

import operator
import time
from scoop import futures


# 模拟工作负载的函数，模拟执行任务时需要的计算时间。
# 这个函数接收一个可迭代对象 inputData，模拟其工作负载（这里通过 time.sleep 模拟一个小延迟），
# 然后返回传入数据的总和。目的是用来测试并行计算的时间效率。
def simulateWorkload(inputData):
    time.sleep(0.01)  # 模拟耗时任务，延迟 0.01 秒
    return sum(inputData)  # 返回 inputData 中所有元素的总和


# 计时器装饰器函数，用于统计函数执行所花费的时间。
# 装饰器的作用是将一个函数包装起来，增加额外的功能（比如这里的计时功能）。
# 装饰器返回一个新的函数（wrapper），它在调用时先记录开始时间，然后执行原函数，最后计算并打印运行时间。
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # 记录开始时间，使用高精度计时器
        result = func(*args, **kwargs)  # 调用被装饰的函数，并获取返回值
        elapsed_time = time.perf_counter() - start_time  # 计算函数运行结束后的时间差
        print(
            f"{func.__name__} executed in {elapsed_time:.3f} seconds"
        )  # 打印函数名和运行时间
        return result  # 返回原函数的返回值

    return wrapper  # 返回包装后的函数


# 使用 SCOOP 的 mapReduce 方法进行并行计算
# futures.mapReduce 需要三个参数：
# 1. 第一个参数 simulateWorkload 是需要并行计算的任务函数。
# 2. 第二个参数 operator.add 是 reduce 阶段的函数，负责合并 map 阶段的结果，类似于累加器。
# 3. 第三个参数是可迭代对象（这里是一个列表），每个元素都会被传递给任务函数 simulateWorkload。
@time_it
def scoop_map_reduce():
    # 为了避免 `generator` 类型没有长度 (len) 的问题，我们将生成器表达式转换为列表。
    # 这里生成了一个 1000 个子列表的列表，每个子列表由重复的数字构成。
    # 例如，第一个子列表是 [0]，第二个是 [1, 1]，第三个是 [2, 2, 2]，依此类推。
    iterable = list([a] * a for a in range(1000))
    # 使用 SCOOP 进行并行计算，每个任务（每个子列表）分配到不同的工作线程。
    # 最后通过 reduce 操作，将每个任务的结果累加在一起，最终返回总和。
    return futures.mapReduce(simulateWorkload, operator.add, iterable)


# 使用 Python 内置的 map() 函数进行串行计算，配合 reduce 操作 (sum) 计算结果。
# map 函数负责将每个可迭代对象传递给 simulateWorkload 函数，并得到其返回结果。
# reduce 操作直接用 sum 函数来汇总所有结果。
@time_it
def python_map_reduce():
    # 同样将生成器表达式转为列表，避免 `generator` 没有 len() 方法的错误。
    iterable = list([a] * a for a in range(1000))
    # 使用 Python 内置的 map 函数，将每个子列表传递给 simulateWorkload 进行处理，
    # 然后用 sum 函数来计算所有结果的总和。
    return sum(map(simulateWorkload, iterable))


# 对比两种 MapReduce 实现方式（SCOOP 并行 vs Python 串行）的执行时间和结果
# 这个函数会分别调用 scoop_map_reduce 和 python_map_reduce 函数，计算并打印它们的执行时间和结果。
def CompareMapReduce():
    # 调用 SCOOP 并行计算
    scoop_result = scoop_map_reduce()  # 并行执行并返回结果
    print(f"SCOOP result: {scoop_result}")  # 打印 SCOOP 的最终结果

    # 调用 Python 串行计算
    python_result = python_map_reduce()  # 串行执行并返回结果
    print(f"Python result: {python_result}")  # 打印 Python 的最终结果


# 主程序入口
# 如果脚本是作为主程序运行，则执行 CompareMapReduce 来对比并行和串行计算。
if __name__ == "__main__":
    CompareMapReduce()
