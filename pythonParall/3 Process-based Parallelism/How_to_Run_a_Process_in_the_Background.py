import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s " % name)
    time.sleep(3)
    print("Exiting %s " % name)


if __name__ == "__main__":
    background_process = multiprocessing.Process(name="background_process", target=foo)
    background_process.daemon = True  # 在后台运行进程, 主进程结束后会自动结束
    NO_background_process = multiprocessing.Process(
        name="NO_background_process", target=foo
    )
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
