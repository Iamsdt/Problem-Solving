from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        dp = [{} for _ in range(len(nums))]
        max_length = 2
        for i in range(len(nums)):
            for jj in range(i):
                diff = nums[i] - nums[jj]
                dp[i][diff] = dp[jj].get(diff, 1) + 1
                max_length = max(max_length, dp[i][diff])

        return max_length
