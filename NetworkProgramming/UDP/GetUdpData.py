import socket

def main():

    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2、绑定本地信息
    localaddr = ("",7788)
    udp_socket.bind(localaddr)

    # 3、接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024) # 1024表示接收的最大数据

        # 4、打印接收到的数据
        # recv_data变量中存储的是一个元组
        recv_msg = recv_data[0] # 数据
        send_addr = recv_data[1] # id地址和端口号
        print("%s：%s"%(str(send_addr),recv_msg.decode("gbk")))

    # 5、关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()