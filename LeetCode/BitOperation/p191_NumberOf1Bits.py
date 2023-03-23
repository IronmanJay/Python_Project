#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res+=1;
            n &= n - 1
        return res

if __name__ == '__main__':
    solution = Solution()
    n = 0o0000000000000000000000000001011
    res = solution.hammingWeight(n)
    print(res)