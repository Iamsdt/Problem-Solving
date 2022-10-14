class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add(node,k):
            if(node):
                if(k==depth-1):
                    temp=node.left
                    node.left=TreeNode(val)
                    node.left.left=temp
                    temp=node.right
                    node.right=TreeNode(val)
                    node.right.right=temp
                    return
                else:
                    add(node.left,k+1)
                    add(node.right,k+1)
            
        
        if(depth==1):
            a=TreeNode(val)
            a.left=root
            return a
        add(root,1)
        return root