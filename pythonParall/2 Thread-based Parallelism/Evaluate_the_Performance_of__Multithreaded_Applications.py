# GIL（Global Interpreter Lock，全局解释器锁）是Python解释器中的一个机制。它的作用是防止多个线程同时执行Python字节码。
# 换句话说，即使在多核处理器上，GIL也只允许一个线程在任何时刻执行Python代码
# GIL并没有影响多处理器并行的线程，只是限制了一个解释器只能有一个线程在运行

from threading import Thread


class threads_object(Thread):
    def run(self):
        function_to_run()


class nothreads_object(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


# 测试用函数
def function_to_run():
    import urllib.request

    req = urllib.request.Request(
        "https://www.packtpub.com/", headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req) as f:
        f.read(1024)


def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))


if __name__ == "__main__":
    import sys
    from timeit import Timer

    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print("Starting tests")
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threaded (%s iters)" % i, best_result)
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)
        print("Iterations complete")
