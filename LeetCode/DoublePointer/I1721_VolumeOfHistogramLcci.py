#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        while left <= right:
            if leftMax < rightMax:
                res += max(0,leftMax-height[left])
                leftMax = max(leftMax,height[left])
                left+=1
            else:
                res += max(0,rightMax-height[right])
                rightMax = max(rightMax,height[right])
                right-=1
        return res

if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = solution.trap(height)
    print(res)
