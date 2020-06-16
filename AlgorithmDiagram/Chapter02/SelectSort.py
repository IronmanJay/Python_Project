def findSmallest(arr):
    """找出数组中最小的元素"""
    smallest = arr[0]  # 存储最小的值，先假设数组中第一个元素就是最小的
    smallest_index = 0  # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """选择排序"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # 找出数组中最小的元素
        newArr.append(arr.pop(smallest))  # 把最小的元素加入新数组中
    return newArr


arr = [5, 3, 6, 2, 10]

result = selectionSort(arr)

print(result)
