# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        
        slow, fast = head, head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    # temp = head
    # for i in [3,4,7,1,2,6]:
    #     temp.next = ListNode(i)
    #     temp = temp.next

    res = Solution().deleteMiddle(head)
    temp = res
    while temp:
        print(temp.val, end=" ")
        temp = temp.next

    print([1,3,4,1,2,6])