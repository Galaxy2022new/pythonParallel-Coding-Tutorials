from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"Hello from process {rank} out of {size}")

    # 进行并行计算


if __name__ == "__main__":
    main()


# 在MPI中，并行程序中不同进程用一个非负的整数来区别，叫做rank。
# 如果我们有p个进程，那么rank会从 0 到 p-1 分配。
# MPI中拿到rank的函数如下：
# rank = comm.Get_rank()

# 这个函数返回调用它的进程的rank。 comm 叫做交流者（Communicator），用于区别不同的进程集合：
# comm = MPI.COMM_WORLD
