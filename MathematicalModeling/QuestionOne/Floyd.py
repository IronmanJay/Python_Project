# 表示两点不连接
inf = float('inf')
# 邻接矩阵
matrix = [[0, 2, inf, 4, 5, inf, inf, inf, inf, inf, inf, inf, inf],
                   [1, 0, 3, 4, inf, inf, inf, inf, inf, inf, inf, inf, inf],
                   [inf, 2, 0, 4, inf, inf, inf, 8, 9, inf, inf, inf, inf],
                   [1, 2, 3, 0, 5, 6, 7, inf, inf, inf, inf, inf, inf],
                   [1, inf, inf, 4, 0, 6, inf, inf, inf, inf, inf, inf, inf],
                   [inf, inf, inf, 4, 5, 0, 7, inf, inf, inf, inf, 12, 13],
                   [inf, inf, inf, 4, inf, 6, 0, inf, inf, inf, 11, 12, inf],
                   [inf, inf, 3, inf, inf, inf, inf, 0, 9, inf, inf, inf, inf],
                   [inf, inf, 3, inf, inf, inf, inf, 8, 0, 10, 11, inf, inf],
                   [inf, inf, inf, inf, inf, inf, inf, inf, 9, 0, 11, inf, 13],
                   [inf, inf, inf, inf, inf, inf, 7, inf, 9, 10, 0, 12, 13],
                   [inf, inf, inf, inf, inf, 6, 7, inf, inf, inf, 11, 0, 13],
                   [inf, inf, inf, inf, inf, 6, inf, inf, inf, 10, 11, 12, 0]]

# Floyd算法计算最短路径（无向图），时间复杂度为O(N^3)
def Floyd_ShortPath(matrix):
    # 基于动态规划思想
    nums_len = len(matrix[0])
    # 外层遍历
    for k in range(nums_len):
        for i in range(nums_len):
            for j in range(nums_len):
                # 更新最短路程
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    # 返回结果
    return matrix


# 打印规划后的邻接矩阵
print(Floyd_ShortPath(matrix))
