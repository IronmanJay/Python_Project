#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == '__main__':
    solution = Solution()
    n = 1
    res = solution.isPowerOfTwo(n)
    print(res)
