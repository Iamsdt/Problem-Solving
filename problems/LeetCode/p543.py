# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]



class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0
        self.diameter(root)
        return self.d
        
    def diameter(self, node):
        if not node: return 0
        l, r = self.diameter(node.left), self.diameter(node.right)
        self.d = max(self.d, l+r)
        return max(l, r) + 1

    
if __name__ == "__main__":
    tree = TreeNode(
        val= 1,
        left=TreeNode(
            val=2,
            left=TreeNode(4),
            right=TreeNode(5)
        ),
        right=TreeNode(4)
    )

    tree = TreeNode(
        val= 1,
        # left=TreeNode(
        #     val=2,
        #     left=TreeNode(4),
        #     right=TreeNode(5)
        # ),
        right=TreeNode(2)
    )

    print(Solution().diameterOfBinaryTree(tree))