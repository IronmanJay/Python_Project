def binary_search(list, target):
    """二分查找"""
    low = 0;
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2  # 在python这里如果单斜杠就是float，需要双斜杠取整或者在前面强制类型转换为int
        if target == list[mid]:  # 如果找到则返回
            return mid
        if target < list[mid]:  # 如果目标值小于中间值，说明目标值在左边，则向左边查找
            high = mid - 1
        else:
            low = mid + 1  # 另外一种情况就是目标值大于中间值，说明目标值在右边，则向右边查找
    return None  # 说明没有找到

list = [1, 3, 5, 7, 9]

res = binary_search(list, 1)

print("在数组中的位置为：" + str(res))
