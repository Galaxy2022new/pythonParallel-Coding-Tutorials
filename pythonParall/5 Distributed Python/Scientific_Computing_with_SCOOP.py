# Scalable Concurrent Operations in Python (SCOOP) 是一个可扩展的 Python 并行计算库，可以将并行的任务（Python 的 Futures ）放到各种各样的计算节点上执行。
# 它基于 ØMQ 架构，提供了一种在分布式系统中管理 Futures 的方法。SCOOP 主要的应用场景是科学计算，尽可能利用所有的结算资源来执行大量的分布式任务
# 以并行执行一个蒙卡特罗算法解决问题展示 SCOOP。下面以计算 π 为例
import math
from random import random
from scoop import futures
from time import time


# 评估落在单位圆内的点数
def evaluate_points_in_circle(num_attempts):
    # 随机的产生点的坐标 (x, y) ，然后判断此点是否落在单位面积的内切圆内。
    points_in_circle = sum(
        1 for _ in range(num_attempts) if math.sqrt(random() ** 2 + random() ** 2) < 1
    )
    # 每当判断点落在圆的面积内的时候， points_in_circle 变量的值加 1
    return points_in_circle


# Monte Carlo方法计算pi值
def pi_montecarlo(workers, num_attempts):
    print(f"线程数: {workers}, 尝试次数: {num_attempts}")
    start_time = time()

    # 并行执行评估函数
    points_in_circle = sum(
        futures.map(evaluate_points_in_circle, [num_attempts] * workers)
    )

    print(f"落在圆内的点数 = {points_in_circle}")

    # 计算pi值，点落在圆内的实际概率是 π / 4
    pi_estimate = 4.0 * points_in_circle / (workers * num_attempts)
    elapsed_time = time() - start_time

    # 打印结果
    print(f"pi估计值 = {pi_estimate}")
    print(f"误差百分比 = {abs(pi_estimate - math.pi) * 100 / math.pi}%")
    print(f"耗时: {elapsed_time:.4f} 秒\n")


if __name__ == "__main__":
    for i in range(1, 4):
        # 使用更多的线程和更大的尝试次数
        pi_montecarlo(i * 1000, i * 1000)
# 如果我们增加 attempts 的次数和 worker 的数量，就可以提高 π 的精度
