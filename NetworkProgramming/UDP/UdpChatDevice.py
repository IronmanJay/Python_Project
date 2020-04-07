import socket

def recv_msg(udp_socket):
    """接收数据"""
    # 使用套接字收发数据
    recv_data = udp_socket.recvfrom(1024)
    # 接收回送过来的数据
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

def send_msg(udp_socket):
    """发送消息"""
    # 获取对方的ip/port/数据
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))
    send_data = input("请输入要发送的数据:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定端口号
    udp_socket.bind(("",7890))
    # 聊天核心功能
    while True:
        print("-----IronmanJay聊天器-----")
        print("-----1:发送消息-----")
        print("-----2:接收消息-----")
        print("-----3:退出系统-----")
        op = input("请输入功能:")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接受并显示
            recv_msg(udp_socket)
        elif op == "3":
            break
        else:
            print("输入有误请重新输入！")
    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()