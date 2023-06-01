#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)
        res = 0
        index = [-1]
        for i in range(0,size):
            if nums[i] & 1 == 1:
                index.append(i)
        index.append(size)
        for i in range(1,len(index) - k):
            res += (index[i] - index[i - 1]) * (index[i + k] - index[i + k - 1])
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2, 1, 1]
    k = 3
    res = solution.numberOfSubarrays(nums,k)
    print(res)
