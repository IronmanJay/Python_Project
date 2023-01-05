#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            n = -n
            x = 1 / x
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    x = 2.00000
    n = 10
    res = solution.myPow(x,n)
    print(res)