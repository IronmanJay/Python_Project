#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(1,n+1):
            for j in range(len(res) - 1,-1,-1):
                res.append(head + res[j])
            head <<= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    n = 2
    res = solution.grayCode(n)
    print(res)