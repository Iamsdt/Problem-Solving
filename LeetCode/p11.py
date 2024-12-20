from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p, q = 0, len(height) - 1
        max_area = 0
        while p < q:
            max_area = max(max_area, min(height[p], height[q]) * (q - p))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1

        return max_area