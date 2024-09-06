# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


if __name__ == "__main__":
    root1 = TreeNode(1,
                     left=TreeNode(3, left=TreeNode(5, )),
                     right=TreeNode(2, )
                     )

    root2 = TreeNode(2,
                     left=TreeNode(1, right=TreeNode(4, )),
                     right=TreeNode(3, right=TreeNode(7))
                     )

    res = Solution().mergeTrees(root1, root2)

    # traverse
    stack = [res]
    output = []
    while stack:
        cv = stack.pop()
        output.append(cv.val)
        if cv.right:
            stack.append(cv.right)
        if cv.left:
            stack.append(cv.left)

    print("OUTPUT: ", output)
