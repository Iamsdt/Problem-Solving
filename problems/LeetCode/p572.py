# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution:
# 1. dfs and compare each node with second root node
# if value is same then compare tree (same as leet 100)
# if it is same then return True, else continue dfs
# to compare, check 
#  both null -> True, if both not null then compare it's value
# if values are same recursive call of both left and right
# otherwise return False

        
class Solution:
    def check(self, p, q):
        if not p and not q:
            return True

        if (p and q) and (p.val == q.val):
            return self.check(p.left, q.left) and self.check(p.right, q.right)

        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            cu = stack.pop()

            if cu.val == subRoot.val:
                # then start matching
                res = self.check(cu, subRoot)
                if res:
                    return True    
            
            if cu.right:
                stack.append(cu.right)
            if cu.left:
                stack.append(cu.left)

        return False


# solution 2:

# Solution:
# if t is null, then it's true and if s is null, then it's false
# check if s and t are subtree, if yes then return true
# else compare t with s.left and s.right
# to compare, check 
#  both null -> True, if both not null then compare it's value
# if values are same recursive call of both left and right
# otherwise return False

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        
        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False
                                    

if __name__ == "__main__":
    tree = TreeNode(
        val= 5,
        left=TreeNode(
            val=4,
            left=TreeNode(1),
            right=TreeNode(2)
        ),
        right=TreeNode(6)
    )

    tree2 = TreeNode(
        val= 4,
        left=TreeNode(5),
        right=TreeNode(2)
    )

    print(Solution().isSubtree(tree, tree2))