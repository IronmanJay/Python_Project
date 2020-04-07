import time
import threading
'''
def sing():
    for x in range(1,6):
        print('我在唱什么')
        time.sleep(1)
def dance():
    for x in range(1,6):
        print('我在跳舞')
        time.sleep(1)
def main():
    sing()
    dance()
if __name__ == '__main__':
    main()
'''
def sing(a):
    print('线程为%s,接收过来的参数为%s'%(threading.current_thread().name,a))
    for x in range(1,6):
        print('我在唱舞娘')
        time.sleep(1)
def dance(a):
    print('线程为%s,接收过来的参数为%s'%(threading.current_thread().name,a))
    for x in range(1,6):
        print('我在跳钢管舞')
        time.sleep(1)
def main():
    a = '孙悟空'
    tsing = threading.Thread(target=sing,name="唱歌",args=(a, ))
    tdance = threading.Thread(target=dance,name="跳舞",args=(a, ))
    tsing.start()
    tdance.start()
    tsing.join()
    tdance.join()
    print('这里是主线程')
if __name__ == '__main__':
    main()