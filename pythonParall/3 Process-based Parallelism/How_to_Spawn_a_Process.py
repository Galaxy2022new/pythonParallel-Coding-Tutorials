# 创建进程对象
# 调用 start() 方法，开启进程的活动
# 调用 join() 方法，在进程结束之前一直等待
import multiprocessing


def foo(i):
    print("called function in process: %s" % i)
    return


if __name__ == "__main__":
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
