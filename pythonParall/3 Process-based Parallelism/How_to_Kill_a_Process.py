import multiprocessing
import time


def foo():
    print("Starting function")
    time.sleep(0.1)
    print("Finished function")


if __name__ == "__main__":
    p = multiprocessing.Process(target=foo)
    # 用 is_alive() 方法监控它的声明周期
    print("Process before execution:", p, p.is_alive())
    p.start()
    print("Process running", p, p.is_alive())
    p.terminate()
    print("Process terminated", p, p.is_alive())
    p.join()
    print("Process joined", p, p.is_alive())
    print("Process exit code", p.exitcode)  # 负数表示子进程被数字为15的信号杀死。

# ExitCode 可能的值如下：
# == 0: 没有错误正常退出
# > 0: 进程有错误，并以此状态码退出
# < 0: 进程被 -1 * 的信号杀死并以此作为 ExitCode 退出
