import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("",7890))

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的内容：")

        # 如果输入的数据是exit，那么就退出程序
        if send_data == "exit":
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto(b"hahaha",('192.168.44.1',8080))
        udp_socket.sendto(send_data.encode("utf-8"), ('192.168.44.1', 8080))

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()