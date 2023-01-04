#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

if __name__ == '__main__':
    solution = Solution()
    num = 38
    res = solution.addDigits(num)
    print(res)