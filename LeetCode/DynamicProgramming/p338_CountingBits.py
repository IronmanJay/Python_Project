#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

from typing import List


class p338_CountingBits:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        res[0] = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = res[i // 2] + 1
        return res


if __name__ == '__main__':
    solution = p338_CountingBits()
    n = 2
    res = solution.countBits(n)
    print(res)