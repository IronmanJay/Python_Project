#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author：IronmanJay
# email：1975686676@qq.com
from typing import Optional


class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root,minVal):
            if root is None:
                return -1
            if root.val > minVal:
                return root.val
            left = dfs(root.left,minVal)
            right = dfs(root.right,minVal)
            if left >= 0 and right >= 0:
                return min(left,right)
            return max(left,right)
        return dfs(root,root.val)

if __name__ == '__main__':
    solution = Solution()
    left = TreeNode(2)
    right = TreeNode(2)
    root = TreeNode(2,left,right)
    res = solution.findSecondMinimumValue(root)
    print(res)