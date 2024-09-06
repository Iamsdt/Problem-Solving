# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution:
# 1. use dfs
# 2. take max from left and right value, if negative then make it zero
# 3. now trick, update global values -> using current nodes (root, left, right)
# 4. now return root value and max(left, right)
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res =  [root.val]

        def dfs(root):    
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val+ left_max+ right_max)

            return root.val + max(left_max, right_max)

        dfs(root)

        return res[0]