#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x,y):
            if temp[x][y] != 0:
                return temp[x][y]
            temp[x][y] += 1
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < m and 0 <= newY < n and matrix[newX][newY] > matrix[x][y]:
                    temp[x][y] = max(temp[x][y],dfs(newX,newY) + 1)
            return temp[x][y]
        m = len(matrix)
        n = len(matrix[0])
        temp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,dfs(i,j))
        return res

if __name__ == '__main__':
    solution = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    res = solution.longestIncreasingPath(matrix)
    print(res)