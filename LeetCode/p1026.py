from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, max_ancestor: int, min_ancestor: int) -> int:
            if node is None:
                return 0

            cu_max = abs(max_ancestor - node.val)
            cu_min = abs(min_ancestor - node.val)
            
            left, right = 0, 0
            if node.left:
                left = dfs(
                    node.left, max(max_ancestor, node.val), min(min_ancestor, node.val))
            
            if root.right:
                right = dfs(
                    node.right, max(max_ancestor, node.val), min(min_ancestor, node.val))
            
            return max(cu_max, cu_min, left, right)
        
        return max(dfs(root.left, root.val, root.val), dfs(root.right, root.val, root.val))


