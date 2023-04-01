#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tempSum = resSum = sum(nums[:k])
        for i in range(k,len(nums)):
            tempSum = tempSum - nums[i - k] + nums[i]
            resSum = max(resSum,tempSum)
        return resSum / k
    
if __name__ == '__main__':
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = solution.findMaxAverage(nums,k)
    print(res)
