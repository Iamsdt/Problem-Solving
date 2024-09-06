# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution:
# use bfs, but queue should list of list, where inner list contains all level nodes
# take first from list of list, and here last element of the inner list is the right view
# for update, iterate inner list and add left and right in a new list
# if new is not empty then add into queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = [[root]]
        while queue:
            cu = queue.pop(0)
            right = cu[-1]
            res.append(right.val)

            v =  []
            for i in cu:
                if i.left:
                    v.append(i.left)
                if i.right:
                    v.append(i.right)

            if v:
                queue.append(v)

        return res


if __name__ == '__main__':
    tree1 = TreeNode(
        val= 1,
        left=TreeNode(
            val=2,
            right=TreeNode(5)
        ),
        right=TreeNode(3, right=TreeNode(4))
    )

    print(Solution().rightSideView(tree1))