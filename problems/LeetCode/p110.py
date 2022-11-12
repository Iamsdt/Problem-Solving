# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


if __name__ == "__main__":
    tree = TreeNode(
        val= 3,
        left=TreeNode(
            val=9,
        ),
        right=TreeNode(
            20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )

    tree2 = TreeNode(
        val= 1,
        left=TreeNode(
            val=2,
            left=TreeNode(
                val=3,
                left=TreeNode(4),
                right=TreeNode(4)
            ),
            right=TreeNode(3)
        ),
        right=TreeNode(
            2
        )
    )

    print(Solution().isBalanced(tree2))