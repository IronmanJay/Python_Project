#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        map = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = []
        while num != 0 and len(res) < 8:
            res.insert(0,map[num & 0xf])
            num >>= 4
        return "".join(res)

if __name__ == '__main__':
    solution = Solution()
    num = 26
    res = solution.toHex(num)
    print(res)
