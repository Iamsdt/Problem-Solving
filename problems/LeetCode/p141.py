# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         # Hash set way
         # Time complexity 0(n)
         # space com o(n)
#         temp = head
        
#         di = {}
        
#         while temp != None:
#             if temp in di:
#                 return True
#             else:
#                 di[temp] = 1
                
#             temp = temp.next

        # Lets use Floyd's Tortoise & Hare
    
        if head == None:
            return False
        
        tortoise = head
        hare = head
        
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
            if hare == tortoise:
                return True
            
        return False


# Algo
# https://medium.com/@tuvo1106/the-tortoise-and-the-hare-floyds-algorithm-87badf5f7d41