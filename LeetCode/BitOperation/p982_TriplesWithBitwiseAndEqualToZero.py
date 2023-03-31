#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter((x & y) for x in nums for y in nums)
        res = 0
        for x in nums:
            for j,k in count.items():
                if (x & j) == 0:
                    res += k
        return res

if __name__ == '__main__':
    soulution = Solution()
    nums = [2, 1, 3]
    res = soulution.countTriplets(nums)
    print(res)

