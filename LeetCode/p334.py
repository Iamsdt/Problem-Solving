from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l, r = float('inf'), float('inf')
              
        for n in nums:
            if n == l or n == r:
                continue
            if n < l:
                l = n
            elif n < r:
                r = n
            else:
                return True
        return False
        


print(Solution().increasingTriplet([20,100,10,12,5,13]))
        