#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - right if citations[right] >= n - right else 0

if __name__ == '__main__':
    solution = Solution()
    citations = [0,1,3,5,6]
    res = solution.hIndex(citations)
    print(res)