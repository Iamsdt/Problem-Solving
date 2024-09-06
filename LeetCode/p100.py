# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution:
# to compare, check 
#  both null -> True, if both not null then compare it's value
# if values are same recursive call of both left and right
# otherwise return False


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q) or (not p or not q):
            return p == q

        if p.val != q.val:
            return False

        # self.isSameTree(p.left, q.left)
        # self.isSameTree(p.right, q.right)

        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))


if __name__ == '__main__':
    tree1 = TreeNode(
        val= 1,
        left=TreeNode(
            val=2
        ),
        right=TreeNode(3)
    )

    tree2 = TreeNode(
        val= 1,
        left=TreeNode(
            val=3
        ),
        right=TreeNode(2)
    )

    print(Solution().isSameTree(tree1, tree2))

