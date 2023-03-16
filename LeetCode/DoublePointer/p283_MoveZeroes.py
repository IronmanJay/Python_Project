#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)