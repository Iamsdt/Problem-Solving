# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head
        while tortoise and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare.val == tortoise.val:
                return True

        return False
