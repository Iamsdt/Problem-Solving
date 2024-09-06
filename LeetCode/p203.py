# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return []

        temp = head

        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
                continue
            
            temp = temp.next

        # for edge cases
        if head.val == val:
            return head.next

        return head




n = ListNode(7)
tm = n
for i in range(5):
    tm.next = ListNode(7)
    tm = tm.next

print(Solution().removeElements(n, 7))