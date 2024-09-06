# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)

        # now reach left position
        lp, cu = dummy, head

        for i in range(left-1):
            lp = lp.next
            cu = cu.next

        # now reverse middle
        