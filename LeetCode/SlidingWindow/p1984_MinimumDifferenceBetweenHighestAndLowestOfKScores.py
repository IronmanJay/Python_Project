#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i] - nums[i - k + 1] for i in range(k - 1,len(nums)))

if __name__ == '__main__':
    solution = Solution()
    nums = [9, 4, 1, 7]
    k = 2
    res = solution.minimumDifference(nums,k)
    print(res)
