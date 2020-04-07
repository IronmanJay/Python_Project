import threading
import time

def test1():
    for i in range(5):
        print("-----Test1---%d--" % i)
        time.sleep(1)

def test2():
    for i in range(10):
        print("-----Test2---%d--" % i)
        time.sleep(1)
    # 如果创建Thread时执行的函数运行结束，那么意味着这个子线程结束了

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)

if __name__ == '__main__':
    main()