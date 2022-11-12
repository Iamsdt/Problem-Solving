# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution
# use string to handle binary, say binary
# append current node value with binary
# if this is leaf node, then append binary into a global array

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []

        def traverse(root, binary=''):
            if not root:
                return

            binary += str(root.val)
            if not root.left and not root.right:
                res.append(binary)

            traverse(root.left, binary)
            traverse(root.right, binary)

        traverse(root)

        return sum([int(binary, 2) for binary in res])
