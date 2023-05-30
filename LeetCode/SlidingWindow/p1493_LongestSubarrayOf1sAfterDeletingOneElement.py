#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        left = 0;
        right = 0;
        zero_count = 0
        res = 0
        while right < size:
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            res = max(res,right - left + 1)
            right += 1
        return res - 1

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 0, 1]
    res = solution.longestSubarray(nums)
    print(res)