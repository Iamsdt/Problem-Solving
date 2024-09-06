# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        def pre(n: Optional[TreeNode]):
            if not n:
                return ""
            s = f"({n.val}"
            if n.right and not n.left:
                s += "()" + pre(n.right) + ")"
            elif n.left and n.right:
                s += pre(n.left) + pre(n.right) + ")"
            elif n.left:
                s += pre(n.left) + ")"
            else:
                s += ")"
            return s

        return f"{root.val}" + ("()" + pre(root.right) if not root.left and root.right \
                                    else pre(root.left) + pre(root.right))


if __name__ == "__main__":
    node = TreeNode(
        1,
        left=TreeNode(
            2, left=TreeNode(4)
        ),
        right=TreeNode(3)
    )

    node2 = TreeNode(
        1,
        left=TreeNode(
            2, right=TreeNode(4)
        ),
        right=TreeNode(3)
    )

    node3 = TreeNode(
        1,
        right=TreeNode(3)
    )

    ans = Solution().tree2str(node)
    ans2 = Solution().tree2str(node2)
    ans3 = Solution().tree2str(node3)
    print(ans3)
    print(ans, ans == "1(2(4))(3)")
    print(ans2, ans2 == "1(2()(4))(3)")
