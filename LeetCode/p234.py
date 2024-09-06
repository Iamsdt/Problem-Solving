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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        prev = slow.next = None
        
        while current:
            t = current.next
            current.next = prev
            prev = current
            current = t

        first, second = head, prev

        while second:
            if second.val != first.val:
                return False

            first = first.next
            second = second.next

        return True

        

if __name__ == "__main__":
    head = ListNode(1)
    temp = head
    temp.next = ListNode(2)
    temp = temp.next

    temp.next = ListNode(2)
    temp = temp.next
    
    temp.next = ListNode(1)
    temp = temp.next

    temp = head
    while temp:
        print(temp.val, sep=",")
        temp = temp.next

    print(Solution().isPalindrome(head))