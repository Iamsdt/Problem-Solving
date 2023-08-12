from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        p = 0
        q = len(nums) - 1

        while p <= q:
            m = (p + q) // 2

            if nums[m] == target:
                return m
            elif nums[m] >= nums[p]:
                if nums[p] <= target <= nums[m]:
                    q = m - 1
                else:
                    p = m + 1
            else:
                if nums[m] <= target <= nums[q]:
                    p = m + 1
                else:
                    q = m - 1

        return -1
