#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def maximum69Number (self, num: int) -> int:
        if num // 1000 == 6:
            return num + 3000
        elif num % 1000 // 100 == 6:
            return num + 300
        elif num % 100 // 10 == 6:
            return num + 30
        elif num % 10 == 6:
            return num + 3
        return num

if __name__ == '__main__':
    solution = Solution()
    num = 9669
    res = solution.maximum69Number(num)
    print(res)