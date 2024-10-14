import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(2)
    print("Finished %s \n" % name)


if __name__ == "__main__":
    # 命名对象的 name 参数
    processes_with_name = multiprocessing.Process(name="foo_Process", target=foo)
    processes_with_default_name = multiprocessing.Process(target=foo)
    processes_with_name.start()
    processes_with_default_name.start()
