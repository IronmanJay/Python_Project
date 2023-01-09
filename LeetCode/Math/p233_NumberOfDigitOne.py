#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def countDigitOne(self, n: int) -> int:
        mul = 1
        res = 0
        while mul <= n:
            res += (n // (mul * 10)) * mul + min(max(n % (mul * 10) - mul + 1,0),mul)
            mul *= 10
        return res

if __name__ == '__main__':
    solution = Solution()
    n = 13
    res = solution.countDigitOne(n)
    print(res)
