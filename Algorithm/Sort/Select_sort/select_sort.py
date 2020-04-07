
def select_sort(alist):
    """选择排序"""
    for j in range(0,len(alist)-1):
        min = j
        for i in range(j+1,len(alist)):
            if alist[min] > alist[i]:
                min = i
        alist[j],alist[min] = alist[min],alist[j]

if __name__ == '__main__':
    li = [54,226,93,17,77,31,44,55,20]
    select_sort(li)
    print(li)