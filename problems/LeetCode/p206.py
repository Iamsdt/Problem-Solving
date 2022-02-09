# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev