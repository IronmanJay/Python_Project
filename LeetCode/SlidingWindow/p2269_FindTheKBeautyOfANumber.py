#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        num = str(num)
        for i in range(0,len(num) - k + 1):
            temp = int(num[i:i+k])
            if temp == 0:
                continue
            if int(num) % temp == 0:
                res += 1
        return res;

if __name__ == '__main__':
    solution = Solution()
    num = 240
    k = 2
    res = solution.divisorSubstrings(num,k)
    print(res)