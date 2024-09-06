from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         p = head
#         temp = head
#         while p and temp:
#             t1 = temp
#             if not t1.next:
#                 break
#             while t1.next.next:
#                 t1 = t1.next

#             # now here temp is the last node
#             t2 = t1.next
#             t1.next = None
#             p = temp.next # 2
#             temp.next = t2 # add 4
#             temp.next.next = p #2 and all
#             temp = p # temp into 2


# solution
# first try to split the list into two
# take fast and slow pointer to find second portion
# for second portion lets reverse the list
# now take fast one from first list and it's next will be the first one from second list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # here slow is the second half
        second = slow.next
        prev = slow.next = None
        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t
        
        # here prev is the reversed list
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next # 2, 3
            first.next = second # 1, 4, 3 (as 4 connected with 3)
            second.next = t1 # 1, 4, 2 (confusion: 3 remain as separate, in t2)
            first, second = t1, t2 # now update pointer
        




if __name__ == "__main__":
    head = ListNode(1)
    temp = head
    for i in range(2, 5):
        temp.next = ListNode(i)
        temp = temp.next
    
    temp = head

    while temp:
        print(temp.val, sep=",")
        temp = temp.next

    Solution().reorderList(head)
    
    print("AFTER")
    temp = head
    while temp:
        print(temp.val, sep=",")
        temp = temp.next