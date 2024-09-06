class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        if val < root.val:
            # then save into left node
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
                
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
            
            
        return root