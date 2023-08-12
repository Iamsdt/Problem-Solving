from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        p, q = 0, len(height) - 1
        res = 0
        while p < q:
            if height[p] < height[q]:
                res += min(height[p], height[q]) - height[p]
                p += 1
            else:
                res += min(height[p], height[q]) - height[q]
                q -= 1

        return res


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
