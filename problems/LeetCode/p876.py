# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Complexity: 
SPACE: o(1)
time: o(n) + o(n/2)

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
SPACE: o(n)
time: o(n)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]