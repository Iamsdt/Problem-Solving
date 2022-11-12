from typing import List
import math


class Solution:
    def signFunc(self, x):
        if x == 0:
            return 0

        return 1 if x > 0 else -1
        
        
    def arraySign(self, nums: List[int]) -> int:
        return self.signFunc(math.prod(nums))



print(Solution().arraySign([-1,-2,-3,-4,3,2,1]))