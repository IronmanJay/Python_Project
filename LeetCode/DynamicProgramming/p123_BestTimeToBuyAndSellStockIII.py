#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i - 1][1],dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2],dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3],dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4],dp[i - 1][3] + prices[i])
        return dp[n - 1][4]

if __name__ == '__main__':
    solution = Solution()
    prices = [3,3,5,0,0,3,1,4]
    res = solution.maxProfit(prices)
    print(res)