#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        if letters[right] <= target:
            return letters[0]
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]

if __name__ == '__main__':
    solution = Solution()
    letters = ['c','f','j']
    target = 'a'
    res = solution.nextGreatestLetter(letters,target)
    print(res)