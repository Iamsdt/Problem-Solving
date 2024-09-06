
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Complexity: 
# SPACE: o(1)
# time: o(n) + o(n/2)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        total = 0
        while temp:
            total +=1 
            temp = temp.next

        mid = total // 2

        temp = head
        total = 0
        while temp:
            if total == mid:
                return temp
            total +=1
            temp = temp.next

        return None


# their solution
# Complexity: 
# SPACE: o(n)
# time: o(n)
class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]



class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head.next
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow


if __name__ == '__main__':
    li = [2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    head = ListNode(1)
    temp = head
    for i in li:
        temp.next = ListNode(i)
        temp = temp.next

    v = Solution2().middleNode(head)
    print(v.val)