import time
import multiprocessing

def test1():
    while True:
        print("1----------------")
        time.sleep(1)

def test2():
    while True:
        print("2----------------")
        time.sleep(1)

def main():
    t1 = multiprocessing.Process(target=test1)
    t2 = multiprocessing.Process(target=test2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()