# asyncio.Futures 类代表还未完成的结果（有可能是一个Exception）。
# 所以综合来说，它是一种抽象，代表还没有做完的事情
# 基本的方法有：
#
# cancel(): 取消future的执行，调度回调函数
# result(): 返回future代表的结果
# exception(): 返回future中的Exception
# add_done_callback(fn): 添加一个回调函数，当future执行的时候会调用这个回调函数
# remove_done_callback(fn): 从“call whten done”列表中移除所有callback的实例
# set_result(result): 将future标为执行完成，并且设置result的值
# set_exception(exception): 将future标为执行完成，并设置Exception

import asyncio
import sys


async def first_coroutine(future, N):
    count = 0
    for i in range(1, N + 1):
        count += i
    await asyncio.sleep(3)
    future.set_result("first coroutine (sum of N integers) result = " + str(count))


async def second_coroutine(future, N):
    count = 1
    for i in range(2, N + 1):
        count *= i
    await asyncio.sleep(4)
    future.set_result("second coroutine (factorial) result = " + str(count))


def got_result(future):
    print(future.result())


if __name__ == "__main__":
    if len(sys.argv) < 3:  # 检查是否有足够的参数
        print("Not enough arguments provided, using default values.")
        N1 = 10  # 默认值
        N2 = 5  # 默认值
    else:
        N1 = int(sys.argv[1])
        N2 = int(sys.argv[2])
    # 创建事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # 使用 asyncio.create_task 将协程转换为任务
    tasks = [
        asyncio.create_task(first_coroutine(future1, N1)),
        asyncio.create_task(second_coroutine(future2, N2)),
    ]

    # 注册回调
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # 等待任务完成
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
