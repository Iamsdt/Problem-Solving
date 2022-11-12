# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





# Depth First Traversals: 
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3 
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3 
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
# Breadth-First or Level Order Traversal: 1 2 3 4 5 


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        
        if root and root.val:    
            data.append(root.val)
        
        if root and root.left:
            data += self.preorderTraversal(root.left)
            
        
        if root and root.right:
            data += self.preorderTraversal(root.right)
            
        return data

    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        