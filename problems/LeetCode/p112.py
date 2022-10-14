class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def check(node, current):
            if not node:
                return False
            
            current += node.val
            if not node.left and not node.right:
                return current == targetSum
            
            return check(node.left, current) or check(node.right, current)
        
        
        return check(root, 0)