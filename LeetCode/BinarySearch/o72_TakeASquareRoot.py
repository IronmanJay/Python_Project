#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
        return left

if __name__ == '__main__':
    solution = Solution()
    x = 8
    res = solution.mySqrt(x)
    print(res)