from typing import List


class Solution:    
    # Time: O(n)
    # Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = {}
        for i in nums:
            if i in di:
                return  True
            else:
                di[i] = 1
        
        return False