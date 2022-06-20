from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        p = 0
        q = 2

        nums.sort()

        value = 0
        
        while q < len(nums):
            if nums[p] + nums[p+1] > nums[q] and nums[p] + nums[q] > nums[p+1] and nums[q] + nums[p+1] > nums[p]:
                value = max(value, (nums[p] + nums[p+1] + nums[q]))

            p+= 1
            q+= 1

        return value


print(Solution().largestPerimeter([3,2,3,4]))