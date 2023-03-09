#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left = [0] * N
        right = [0] * N
        left[0] = 1
        for i in range(1,N):
            left[i] = left[i - 1] + 1 if ratings[i] > ratings[i - 1] else 1
        right[N - 1] = 1
        for i in range(N - 2,-1,-1):
            right[i] = right[i + 1] + 1 if ratings[i] > ratings[i + 1] else 1
        res = 0
        for i in range(0,N):
            res += max(left[i],right[i])
        return res

if __name__ == '__main__':
    solution = Solution()
    ratings = [1,0,2]
    res = solution.candy(ratings)
    print(res)