# Definition for a binary tree node.
from re import T
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        temp = root

        stack = [root.right, root.left]
        while stack:
            cu = stack.pop()
            if not cu:
                continue
            
            temp.left = None
            temp.right = TreeNode(cu.val)
            temp = temp.right

            if cu.right:
                stack.append(cu.right)
            if cu.left:
                stack.append(cu.left)

        