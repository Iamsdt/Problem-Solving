# A monotonic stack is a data structure that maintains its elements in a monotonic order.
# This can be either increasing or decreasing order.
# It is often used in algorithm problems to find the next greater or smaller element.
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        curr, prev.next = prev.next, None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp

        return prev


if __name__ == '__main__':
    nodes = [5, 2, 13, 3, 8]
    head = ListNode(nodes[0])
    cur = head
    for i in nodes[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    s = Solution()
    res = s.removeNodes(head)
    while res:
        print(res.val)
        res = res.next

