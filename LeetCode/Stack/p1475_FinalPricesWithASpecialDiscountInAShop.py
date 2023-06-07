#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        for i in range(0,len(prices)):
            while len(stack) > 1 and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

if __name__ == '__main__':
    solution = Solution()
    prices = [8, 4, 6, 2, 3]
    res = solution.finalPrices(prices)
    print(res)
