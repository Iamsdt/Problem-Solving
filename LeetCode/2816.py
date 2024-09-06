from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linked list
        current = head
        prev = None

        while current:
            val = current.val
            val = val * 2
            current.val = val % 10
            if val >= 10 and prev:
                prev.val += 1
            elif val >= 10:
                head = ListNode(1, current)

            # update pointers
            prev = current
            current = current.next

        return head


if __name__ == "__main__":
    needs = [1, 8, 9]
    head = ListNode(needs[0])
    cur = head
    for i in needs[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    s = Solution()
    value = s.doubleIt(head)
    while value:
        print(value.val)
        value = value.next
