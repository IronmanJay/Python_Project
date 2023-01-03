#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                res += i
                if i * i < num:
                    res += num / i
            i += 1
        return res == num

if __name__ == '__main__':
    solution = Solution()
    num = 28
    res = solution.checkPerfectNumber(num)
    print(res)