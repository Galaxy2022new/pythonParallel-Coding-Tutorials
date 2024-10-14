import Pyro5.api as pyro  # 导入 Pyro5 的 API


def main():
    # 获取用户输入的 Pyro URI 和姓名
    uri = input("What is the Pyro uri of the greeting object? ").strip()
    name = input("What is your name? ").strip()

    # 使用 Pyro 创建远程对象的代理
    server = pyro.Proxy(uri)
    print(server.welcomeMessage(name))  # 调用远程方法并打印返回的欢迎信息


if __name__ == "__main__":
    main()  # 如果是直接运行该脚本，则执行主函数
