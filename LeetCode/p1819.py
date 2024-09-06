import math
from typing import List


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_n = max(nums) + 1
        seen = set(nums)

        ans = 0
        for k in range(1, max_n):  # iterate candidate k
            gcd = 0
            for multiple in range(k, max_n, k):
                print(multiple)
                if multiple in seen:
                    gcd = math.gcd(gcd, multiple)
            if gcd == k:  # check the candidate
                ans += 1
        return ans


if __name__ == "__main__":
    # a = Solution().countDifferentSubsequenceGCDs(
    #     [6, 10, 3]
    # )

    b = 5 / -6
    print(b)
    print((b*10)/10)
    ans = b - b/10
    print(int(ans))
