#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            dif = arr[mid] - mid - 1
            if dif >= k:
                right = mid
            else:
                left = mid + 1
        return k - (arr[left - 1] - (left - 1) - 1) + arr[left - 1]

if __name__ == '__main__':
    solution = Solution()
    arr = [2,3,4,7,11]
    k = 5
    res = solution.findKthPositive(arr,k)
    print(res)