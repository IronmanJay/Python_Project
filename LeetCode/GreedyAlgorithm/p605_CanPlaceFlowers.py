#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        for i in range(0,len(flowerbed)):
            if (flowerbed[i] == 0) and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0) and (i == 0 or flowerbed[i - 1] == 0):
                flowerbed[i] = 1
                res += 1
        return res >= n

if __name__ == '__main__':
    solution = Solution()
    flowered = [1,0,0,0,1]
    n = 1
    res = solution.canPlaceFlowers(flowered,n)
    print(res)