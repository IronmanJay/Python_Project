#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i - 1] + nums[i],nums[i])
            res = max(res,dp[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = solution.maxSubArray(nums)
    print(res)