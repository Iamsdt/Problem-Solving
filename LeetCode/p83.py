from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
                continue
            
            temp = temp.next

        return head



n = ListNode(1)
tm = n
tm.next = ListNode(1)
tm = tm.next
tm.next = ListNode(2)
tm = tm.next
tm.next = ListNode(2)
tm = tm.next
tm.next = ListNode(3)
tm = tm.next
tm.next = ListNode(3)
tm = tm.next

out = Solution().deleteDuplicates(n)
temp = out
while temp:
    print(temp.val)
    temp = temp.next