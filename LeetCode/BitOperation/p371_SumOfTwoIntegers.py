#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

if __name__ == '__main__':
    solution = Solution()
    a = 1
    b = 2
    res = solution.getSum(a,b)
    print(res)
