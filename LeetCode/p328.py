from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head

        odd, even = head, head.next
        while even and even.next:
            temp = even.next
            even.next = even.next.next

            temp.next = odd.next
            odd.next = temp
            
            odd, even = odd.next, even.next
        return head


if __name__ == '__main__':
    li = [2,3,4,5]
    head = ListNode(1)
    temp = head
    for i in li:
        temp.next = ListNode(i)
        temp = temp.next

    temp = head
    inp = []
    while temp:
        inp.append(temp.val)
        temp = temp.next

    print("Input", inp)

    v = Solution().oddEvenList(head)
    temp = v
    ans = []
    while temp:
        ans.append(temp.val)
        temp = temp.next

    print(ans)