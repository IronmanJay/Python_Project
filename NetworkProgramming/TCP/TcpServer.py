import socket

def main():
    # 1、买个手机（创建套接字）
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、插入手机卡（绑定本地信息）
    tcp_server.bind(("",7890))
    # 3、将手机设置为正常的响铃模式（让默认的套接字由主动变为被动）
    tcp_server.listen(128)
    # 循环目的：调用多次accept，从而为多个客户端服务
    while True:
        print("等待一个新的客户端的到来")
        # 4、等待别人的电话到来（等待客户端的链接）
        new_client,client_addr = tcp_server.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))
        # 循环目的：为同一个客户端服务多次
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client.recv(1024)
            print("客户端发送过来的请求是%s" % recv_data.decode("utf-8"))
            # 如果recv解堵塞，那么有两种方式
            # 1、客户端发送过来数据
            # 2、客户端调用close导致recv解堵塞
            if recv_data:
                # 服务端返回数据给客户端
                new_client.send("hahaha".encode("utf-8"))
            else:
                break
        print("已经为这个客户端服务完毕")
        # 关闭套接字
        # 关闭accept返回的套接字意味着不会为这个客户端服务
        new_client.close()
    # 如果将监听套接字关闭了，就会导致不能再次等待新的客户端的到来，即accept失效
    tcp_server.close()

if __name__ == '__main__':
    main()