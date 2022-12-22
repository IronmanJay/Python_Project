#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * (n + 1)
        p2 = 1
        p3 = 1
        p5 = 1
        for i in range(2,n+1):
            dp[i] = min(dp[p2] * 2,dp[p3] * 3,dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    n = 10
    res = solution.nthUglyNumber(n)
    print(res)