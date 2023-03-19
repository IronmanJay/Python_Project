#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        len1 = len(version1)
        len2 = len(version2)
        index1 = 0
        index2 = 0
        while index1 < len1 or index2 < len2:
            x = 0
            while index1 < len1 and version1[index1] != '.':
                x = x * 10 + ord(version1[index1]) - ord('0')
                index1 += 1
            index1 += 1
            y = 0
            while index2 < len2 and version2[index2] != '.':
                y = y * 10 + ord(version2[index2]) - ord('0')
                index2 += 1
            index2 += 1
            if x != y:
                return 1 if x > y else -1
        return 0

if __name__ == '__main__':
    solution = Solution()
    version1 = "1.01"
    version2 = "1.001"
    res = solution.compareVersion(version1,version2)
    print(res)