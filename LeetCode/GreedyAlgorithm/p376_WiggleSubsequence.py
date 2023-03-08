#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        preDiff = nums[1] - nums[0];
        res = 2 if preDiff != 0 else 1
        for i in range(2,len(nums)):
            diff = nums[i] - nums[i - 1]
            if (preDiff >= 0 and diff < 0) or (preDiff <= 0 and diff > 0):
                res+=1
                preDiff = diff
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1,7,4,9,2,5]
    res = solution.wiggleMaxLength(nums)
    print(res)