# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def check_is_leaf(self, node):
        return not node.left and not node.right

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        res = 0

        while stack:
            cu = stack.pop()
            if cu.right:
                stack.append(cu.right)
            
            if cu.left:
                if self.check_is_leaf(cu.left):
                    res += cu.left.val
                else:
                    stack.append(cu.left)

        return res

    # somehow run fast, but why?
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0

        if root.left:
            if self.check_is_leaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

        if root.right:
            res += self.sumOfLeftLeaves(root.right)

        return res