from typing import List

# Date: 18/6/2023


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}

        for i in nums:
            if target - i in di:
                return [di[target - i], i]
            else:
                di[i] = i

        return [-1, -1]
