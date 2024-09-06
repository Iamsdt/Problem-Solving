from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p, q = 0, len(nums) - 1

        while p <= q:
            mid = (p + q) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1

        return -1
