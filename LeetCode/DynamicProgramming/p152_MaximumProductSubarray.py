#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        tempMax = 1
        tempMin = 1
        for i in range(0,len(nums)):
            if nums[i] < 0:
                temp = tempMax
                tempMax = tempMin
                tempMin = temp
            tempMax = max(tempMax * nums[i],nums[i])
            tempMin = min(tempMin * nums[i],nums[i])
            res = max(res,tempMax)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,-2,4]
    res = solution.maxProduct(nums)
    print(res)