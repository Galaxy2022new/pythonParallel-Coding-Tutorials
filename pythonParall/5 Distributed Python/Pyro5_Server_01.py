import Pyro5.api as pyro  # 导入 Pyro5 的 API


@pyro.expose  # 装饰器，表示该类的方法可以被远程调用
class Server(object):
    def welcomeMessage(self, name):
        """返回欢迎信息的方法"""
        return "Hi welcome " + str(name)  # 将名字转换为字符串并返回欢迎信息


def startServer():
    server = Server()  # 创建服务器对象
    daemon = pyro.Daemon()  # 创建 Pyro 守护进程
    ns = pyro.locate_ns()  # 定位名称服务器
    uri = daemon.register(server)  # 注册服务器对象到守护进程，并获取 URI
    ns.register("server", uri)  # 在名称服务器注册服务器对象的 URI
    print("Ready. Object uri =", uri)  # 打印服务器对象的 URI
    daemon.requestLoop()  # 进入请求循环，等待客户端请求


if __name__ == "__main__":
    startServer()  # 如果是直接运行该脚本，则启动服务器


# 终端运行 python -m Pyro5.nameserver
# 结果：
# Not starting broadcast server for IPv6.
# NS running on localhost:9090 (::1)
# URI = PYRO:Pyro.NameServer@localhost:9090
