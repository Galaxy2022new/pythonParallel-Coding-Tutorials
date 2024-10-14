# yield表示协程在此暂停，并且将执行权交给其他协程。
# 因为协程可以将值与控制权一起传递给另一个协程，所以“yield一个值”就表示将值传给下一个执行的协程

import asyncio
from random import randint

# 使用 Asyncio 的协程来模拟有限状态机 (FSA)
# Python 现在推荐使用 async def 来定义协程，而不再使用 @asyncio.coroutine


async def StartState():
    print("Start State called \n")
    input_value = randint(0, 1)
    await asyncio.sleep(1)  # 使用异步的暂停代替 time.sleep
    if input_value == 0:
        result = await State2(input_value)
    else:
        result = await State1(input_value)
    print("Resume of the Transition : \nStart State calling " + result)


async def State1(transition_value):
    outputValue = str("State 1 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print("...evaluating...")
    if input_value == 0:
        result = await State3(input_value)
    else:
        result = await State2(input_value)
    result = "State 1 calling " + result
    return outputValue + str(result)


async def State2(transition_value):
    outputValue = str("State 2 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = await State1(input_value)
    else:
        result = await State3(input_value)
    result = "State 2 calling " + result
    return outputValue + str(result)


async def State3(transition_value):
    outputValue = str("State 3 with transition value = %s \n" % transition_value)
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = await State1(input_value)
    else:
        result = await EndState(input_value)
    result = "State 3 calling " + result
    return outputValue + str(result)


async def EndState(transition_value):
    outputValue = str("End State with transition value = %s \n" % transition_value)
    print("...Stop Computation...")
    return outputValue


if __name__ == "__main__":
    print("Finite State Machine simulation with Asyncio Coroutine")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(StartState())
    loop.close()
