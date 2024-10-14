from __future__ import print_function
import Pyro5.api
import P5_Link_Objects_ChainTopology

this = "2"
next = "3"
servername = "example.chainTopology." + this

daemon = Pyro5.server.Daemon()  # 使用 Pyro5 的 server.Daemon
obj = P5_Link_Objects_ChainTopology.Chain(this, next)
uri = daemon.register(obj)

ns = Pyro5.api.locate_ns()  # 找到名称服务器
ns.register(servername, uri)  # 注册对象

print("server_%s started " % this)
daemon.requestLoop()  # 启动服务循环
