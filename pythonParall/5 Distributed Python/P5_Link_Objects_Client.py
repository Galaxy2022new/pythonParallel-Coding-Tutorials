from __future__ import print_function
import Pyro5.api

# 使用 Pyro5 的 Proxy 连接到第一个服务对象
obj = Pyro5.api.Proxy("PYRONAME:example.chain.A")
print("Result=%s" % obj.process(["Hello"]))
