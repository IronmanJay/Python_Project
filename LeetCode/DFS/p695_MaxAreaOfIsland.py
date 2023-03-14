#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            count = 1
            count += dfs(grid,i + 1,j)
            count += dfs(grid,i,j + 1)
            count += dfs(grid,i - 1,j)
            count += dfs(grid,i,j - 1)
            return count

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,dfs(grid,i,j))
        return res

if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,0,0,0,0,0,0]]
    res = solution.maxAreaOfIsland(grid)
    print(res)