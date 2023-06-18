# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        elif list2:
            current.next = list2

        return dummy.next


if __name__ == '__main__':
    # begin
    s = Solution()
    list1 = [2, 4]
    node1 = ListNode(val=1)
    for i in list1:
        node1.next = ListNode(val=1)

    list2 = [1, 3, 4]
    print(s.mergeTwoLists([], []))
