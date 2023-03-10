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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inOrder(root):
            nonlocal res,pre
            if root != None:
                inOrder(root.left)
                if pre != -1:
                    res = min(res,abs(root.val - pre))
                pre = root.val
                inOrder(root.right)
        pre = -1
        res = float('inf')
        inOrder(root)
        return res

if __name__ == '__main__':
    solution = Solution()
    left1 = TreeNode(1)
    left2 = TreeNode(3)
    left = TreeNode(2,left1,left2)
    right = TreeNode(6)
    root = TreeNode(4,left,right)
    res = solution.minDiffInBST(root)
    print(res)
