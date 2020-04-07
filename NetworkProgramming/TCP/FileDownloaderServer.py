import socket

def send_file_2_client(new_client_scoket,client_addr):
    # 一、接收客户端需要下载的文件名
    # 5、接收客户端发送来的要下载的文件名
    file_name = new_client_scoket.recv(1024).decode()
    print("客户端%s需要下载的文件是%s" % (str(client_addr), file_name))
    file_content = None
    # 二、打开这个文件，读取数据
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件%s" % file_name)
    # 三、发送文件的数据给客户端
    # 6、发送文件的数据给客户端
    if file_content:
        # new_client_scoket.send("hahaha".encode("utf-8"))
        new_client_scoket.send(file_content)

def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2、绑定本地信息
    tcp_socket.bind(("",7890))
    # 3、让默认的套接字由主动变为被动
    tcp_socket.listen(128)
    while True:
        # 4、等待客户端的链接
        new_client_scoket,client_addr = tcp_socket.accept()
        # 调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_scoket,client_addr)
        # 7、关闭套接字
        new_client_scoket.close()
    tcp_socket.close()

if __name__ == '__main__':
    main()