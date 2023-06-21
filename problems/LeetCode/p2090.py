from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = 2 * k + 1

        ws = 0
        result = [-1] * n

        if n < window:
            return result

        for i in range(n):
            ws += nums[i]

            if i - window >= 0:
                ws -= nums[i - window]

            elif i >= window - 1:
                result[i - k] = ws // window

        return result
