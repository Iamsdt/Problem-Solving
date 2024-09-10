class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        if sum(nums) < target: return 0

        s, l, ans = 0, 0, len(nums)
        
        for r, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[l]                          
                ans = min(ans, r - l + 1)             
                l+= 1                                 

        return ans
