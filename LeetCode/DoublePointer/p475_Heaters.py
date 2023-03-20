#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        lenHouses = len(houses)
        lenHeaters = len(heaters)
        res = 0
        j = 0
        for i in range(0,lenHouses):
            curDis = abs(houses[i] - heaters[j])
            while j < lenHeaters - 1 and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j+=1
                curDis = abs(houses[i] - heaters[j])
            res = max(res,curDis)
        return res

if __name__ == '__main__':
    solution = Solution()
    houses = [1, 2, 3]
    heaters = [2]
    res = solution.findRadius(houses,heaters)
    print(res)