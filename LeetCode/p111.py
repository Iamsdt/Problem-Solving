# Definition for a binary tree node.
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_leaf(self, node):
        return not node.left and not node.right

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        min_depth = float('inf')

        while stack:
            cu = stack.pop()
            node = cu[1]
            if self.is_leaf(node):
                min_depth = min(min_depth, cu[0])
                continue

            if node.right:
                stack.append((cu[0]+1, node.right))
            
            if node.left:
                stack.append((cu[0]+1, node.left))

        return min_depth
    