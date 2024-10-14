# 两个不同的进程之间可以通过点对点通讯交换数据：一个进程是接收者，一个进程是发送者
# Python的 mpi4py 通过下面两个函数提供了点对点通讯功能：
#
# Comm.Send(data, process_destination): 通过它在交流组中的排名来区分发送给不同进程的数据
# Comm.Recv(process_source): 接收来自源进程的数据，也是通过在交流组中的排名来区分的
# Comm 变量表示交流者，定义了可以互相通讯的进程组：
#
# comm = MKPI.COMM_WORLD

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data % s " % data + "to process % d" % destination_process)

if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print("sending data % s :" % data + "to process % d" % destination_process)

if rank == 4:
    data = comm.recv(source=0)
    print("data received is = % s" % data)

if rank == 8:
    data1 = comm.recv(source=1)
    print("data1 received is = % s" % data1)
