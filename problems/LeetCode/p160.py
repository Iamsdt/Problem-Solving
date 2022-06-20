# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Definition for singly-linked list.
from typing import Optional

from requests import head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2:
            print(f"L1 {l1.val if l1 else -1} and L2: {l2.val if l2 else -1}")
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1


if __name__ == '__main__':
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]

    headA = ListNode(listA[0])
    headB = ListNode(listB[0])

    temp = headA
    for i in listA[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    temp = headB
    for i in listB[1:]:
        temp.next = ListNode(i)
        temp = temp.next


    res = Solution().getIntersectionNode(headA, headB)
    temp = res
    print("Return Value")
    while temp:
        print(temp.val, sep=",")
        temp = temp.next