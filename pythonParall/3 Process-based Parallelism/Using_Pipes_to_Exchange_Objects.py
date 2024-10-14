# 一个管道可以做以下事情：
#
# 返回一对被管道连接的连接对象
# 然后对象就有了 send() 和 recv() 方法 方法可以在进程之间通信
# 管道是全双工的，即每一端都可以进行发送和接收操作

import multiprocessing


def creat_items(pipe):
    output_pipe, _ = pipe  # 获取管道的发送端
    for item in range(10):  # 生成 0 到 9 的数字
        output_pipe.send(item)  # 通过管道的发送端发送数据
    output_pipe.close()  # 关闭管道的发送端


# 从 pipe_1 接收数据，将数据平方后，通过 pipe_2 发送
def multipy_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1  # 获取 pipe_1 的接收端
    close.close()  # 关闭 pipe_1 的发送端
    output_pipe, _ = pipe_2  # 获取 pipe_2 的发送端
    try:
        while True:
            item = input_pipe.recv()  # 从 pipe_1 的接收端接收数据
            output_pipe.send(item * item)  # 将数据平方后通过 pipe_2 发送
    except EOFError:
        output_pipe.close()  # 当接收到 EOFError 时，关闭 pipe_2 的发送端


if __name__ == "__main__":
    pipe_1 = multiprocessing.Pipe()  # 创建管道 1
    process_pipe_1 = multiprocessing.Process(
        target=creat_items, args=(pipe_1,)
    )  # 创建并启动 creat_items 进程
    process_pipe_1.start()

    pipe_2 = multiprocessing.Pipe()  # 创建管道 2
    process_pipe_2 = multiprocessing.Process(
        target=multipy_items, args=(pipe_1, pipe_2)
    )  # 创建并启动 multipy_items 进程
    process_pipe_2.start()

    pipe_1[0].close()  # 关闭 pipe_1 的接收端，因为当前进程不需要从 pipe_1 接收数据
    pipe_2[0].close()  # 关闭 pipe_2 的发送端，因为当前进程不需要向 pipe_2 发送数据

    try:
        while True:
            print(pipe_2[1].recv())  # 不断从 pipe_2 中接收数据并打印
    except EOFError:
        print("End")  # 当接收到 EOFError 时，说明管道已关闭，结束循环
