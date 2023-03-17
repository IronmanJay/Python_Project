#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        size = len(arr)
        i = -1
        top = 0
        while top < size:
            i+=1
            if arr[i] == 0:
                top+=2
            else:
                top+=1
        j = size - 1
        if top == size + 1:
            arr[j] = 0
            j-=1
            i-=1
        while j >= 0:
            arr[j] = arr[i]
            j-=1
            if arr[i] == 0:
                arr[j] = arr[i]
                j-=1
            i-=1

if __name__ == '__main__':
    solution = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(arr)
    print(arr)