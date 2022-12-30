#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0,n):
            for j in range(i + 1,n):
                left = j + 1
                right = n - 1
                k = j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] >= nums[i] + nums[j]:
                        right = mid - 1
                    else:
                        k = mid
                        left = mid + 1
                res += k - j
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,3,4]
    res = solution.triangleNumber(nums)
    print(res)