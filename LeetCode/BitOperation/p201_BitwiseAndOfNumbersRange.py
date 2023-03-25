#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count

if __name__ == '__main__':
    solution = Solution()
    left = 5
    right = 7
    res = solution.rangeBitwiseAnd(left,right)
    print(res)
