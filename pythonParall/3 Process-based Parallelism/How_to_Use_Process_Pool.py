# Pool 类有以下方法：
#
# apply(): 直到得到结果之前一直阻塞。
# apply_async(): 这是 apply() 方法的一个变体，返回的是一个result对象。这是一个异步的操作，在所有的子类执行之前不会锁住主进程。
# map(): 这是内置的 map() 函数的并行版本。在得到结果之前一直阻塞，此方法将可迭代的数据的每一个元素作为进程池的一个任务来执行。
# map_async(): 这是 map() 方法的一个变体，返回一个result对象。如果指定了回调函数，回调函数应该是callable的，并且只接受一个参数。
#   当result准备好时会自动调用回调函数（除非调用失败）。回调函数应该立即完成，否则，持有result的进程将被阻塞。

import multiprocessing


def function_square(data):
    result = data * data
    return result


if __name__ == "__main__":
    inputs = list(range(100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print("Pool:", pool_outputs)
# pool.map() 方法的结果和Python内置的 map() 结果是相同的，
# 不同的是 pool.map() 是通过多个并行进程计算的
