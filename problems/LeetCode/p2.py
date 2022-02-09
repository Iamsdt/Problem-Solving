class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        # add fake head
        head = current = ListNode(0)
        while l1 or l2:
            val = res
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            current.next = ListNode(val % 10)
            current = current.next
            res = val // 10
        if res > 0:
            current.next = ListNode(res)
        return head.next