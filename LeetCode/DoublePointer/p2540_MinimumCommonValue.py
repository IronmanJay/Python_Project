#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = 0
        index2 = 0
        while index1 < len1 and index2 < len2:
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            elif nums1[index1] < nums2[index2]:
                index1+=1
            elif nums1[index1] > nums2[index2]:
                index2+=1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4]
    res = solution.getCommon(nums1,nums2)
    print(res)