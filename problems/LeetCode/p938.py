# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        stack = [root]
        res = 0

        while stack:
            cu = stack.pop()
            if low <= cu.val <= high:
                res += cu.val

            if cu.right:
                stack.append(cu.right)
            if cu.left:
                stack.append(cu.left)

        return res

