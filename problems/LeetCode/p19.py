# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow, fast = dummy, head
        
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next is the node, we have to remove
        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    temp = head
    for i in range(2, 10):
        temp.next = ListNode(i)
        temp = temp.next
    
    temp = head

    while temp:
        print(temp.val, sep=",")
        temp = temp.next

    head = Solution().removeNthFromEnd(head, 2)
    
    print("AFTER")
    temp = head
    while temp:
        print(temp.val, sep=",")
        temp = temp.next