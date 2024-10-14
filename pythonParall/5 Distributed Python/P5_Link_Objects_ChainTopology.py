# 定义链中的处理对象，即每个服务器的核心逻辑
from __future__ import print_function
import Pyro5.api


# 定义链式对象
class Chain(object):
    def __init__(self, name, next_name):
        self.name = name
        self.next_name = next_name
        self.next = None

    @Pyro5.api.expose  # 通过 @expose 公开此方法
    def process(self, message):
        if self.next is None:
            # 创建指向下一个对象的代理
            self.next = Pyro5.api.Proxy(
                "PYRONAME:example.chainTopology." + self.next_name
            )

        if self.name in message:
            print(f"Back at {self.name}; the chain is closed!")
            return [f"complete at {self.name}"]
        else:
            print(f"{self.name} forwarding the message to the object {self.next_name}")
            message.append(self.name)
            result = self.next.process(message)
            result.insert(0, f"passed on from {self.name}")
            return result
