
def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(alist) - 1):
        count = 0
        for i in range(0,len(alist) - 1 - j):
            # 从头走到尾
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return

if __name__ == '__main__':
    li = [54,26,91,17,31,44,55,20]
    bubble_sort(li)
    print(li)