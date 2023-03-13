#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(0,m):
            for j in range(0,n):
                if (board[i][j] == 'X') and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    count+=1
        return count

if __name__ == '__main__':
    a1 = ["X",".",".","X"]
    a2 = [".",".",".","X"]
    a3 = [".",".",".","X"]
    b = [a1,a2,a3]
    solution = Solution()
    res = solution.countBattleships(b)
    print(res)