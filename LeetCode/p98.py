from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return check(node.left, left, node.val) and check(node.right, node.val, right)
        
        
        return check(root, float("-inf"), float("inf"))