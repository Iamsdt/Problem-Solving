from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        for i in range(1, len(nums)):
            s = m - i
