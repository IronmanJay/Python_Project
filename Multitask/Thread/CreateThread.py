import threading
import time

def test1():
    for i in range(5):
        print("-----Test1---%d--" % i)
        time.sleep(1)

def main():
    # 在调用thread之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    # 在调用thread之后先打印当前线程信息
    print(threading.enumerate())
    t1.start()
    # 在调用start之后先打印当前线程信息
    print(threading.enumerate())

if __name__ == '__main__':
    main()