from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        alt = 0
        for i in gain:
            alt += i
            res = max(res, alt)

        return res


if __name__ == "__main__":
    print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
