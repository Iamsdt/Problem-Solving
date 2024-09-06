# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def minimum(self, node):
        if not node:
            return float('inf')
        
        if node.left and node.right:
            return min(node.left.val, node.right.val)

        if node.left:
            return node.left.val
        elif node.right:
            return node.right.val

        return node.val



    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        first_min = float('inf')
        second_min = float('inf')

        while stack:
            cu = stack.pop()
            
            m = self.minimum(cu)

            first_min = min(m, first_min)
            if first_min < cu.val <= second_min:
                second_min = cu.val

            if cu.right:
                stack.append(cu.right)
        
            if cu.left:
                stack.append(cu.left)


        return second_min if second_min != float('inf') else -1


if __name__ == '__main__':
    tree = TreeNode(2, TreeNode(2), TreeNode(2))
    print(Solution().findSecondMinimumValue(tree))