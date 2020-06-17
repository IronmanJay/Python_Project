def quictSort(array):
    """快速排序"""
    if len(array) < 2:
        return array  # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]  # 选取子表的第一个元素为基准值
        less = [i for i in array[1:] if i <= pivot]  # 由所有小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组
        return quictSort(less) + [pivot] + quictSort(greater)


array = [10, 5, 2, 3]

res = quictSort(array)

print(res)
