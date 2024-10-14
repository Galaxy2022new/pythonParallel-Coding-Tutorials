# 实现一个自定义的进程子类
# 定义 Process 的子类
# 覆盖 __init__(self [,args]) 方法来添加额外的参数
# 覆盖 run(self, [.args]) 方法来实现 Process 启动的时候执行的任务

import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print("called run method in process: %s" % self.name)
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()
        print(p)