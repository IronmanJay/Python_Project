
def quick_sort(alist,first,last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 循环退出后，low==high，min_value插入此位置
    alist[low] = mid_value
    # 开始对low左边的列表进行快速排序
    quick_sort(alist,first,low-1)
    # 开始对low右边的列表进行快速排序
    quick_sort(alist,low+1,last)

if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    quick_sort(li,0,len(li)-1)
    print(li)