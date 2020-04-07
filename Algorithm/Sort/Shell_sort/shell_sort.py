
def shell_sort(alist):
    """希尔排序"""
    gap = len(alist) // 2
    while gap > 0:
        for j in range(gap,len(alist)):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == '__main__':
    li = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(li)
    print(li)