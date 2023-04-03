#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sumW = 0
        for i in range(k):
            if blocks[i] == 'W':
                sumW += 1
        res = sumW
        for i in range(k,len(blocks)):
            if blocks[i] == 'W':
                sumW += 1
            if blocks[i - k] == 'W':
                sumW -= 1
            res = min(res,sumW)
        return res

if __name__ == '__main__':
    solution = Solution()
    blocks = "WBBWWBBWBW"
    k = 7
    res = solution.minimumRecolors(blocks,k)
    print(res)
