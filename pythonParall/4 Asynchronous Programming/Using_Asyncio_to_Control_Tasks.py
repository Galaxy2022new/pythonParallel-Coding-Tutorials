# asyncio.Task() 类，可以在任务中使用协程。它的作用是，在同一事件循环中,运行某一个任务的同时可以并发地运行多个任务
# 当协程被包在任务中，它会自动将任务和事件循环连接起来，当事件循环启动的时候，任务自动运行。这样就提供了一个可以自动驱动协程的机制

import asyncio


async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        await asyncio.sleep(1)
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))


async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        await asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))


async def binomialCoeff(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print("Asyncio.Task: Compute binomialCoeff (%s)" % (i))
        await asyncio.sleep(1)
    print("Asyncio.Task - binomialCoeff(%s , %s) = %s" % (n, k, result))


if __name__ == "__main__":
    tasks = [
        asyncio.Task(factorial(10)),
        asyncio.Task(fibonacci(10)),
        asyncio.Task(binomialCoeff(20, 10)),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
